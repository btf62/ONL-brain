#!/usr/bin/env python3
"""Build a private 360 review answer archive from local review PDFs."""

from __future__ import annotations

import csv
import glob
import json
import os
import re
import sqlite3
import subprocess
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


SOURCE_DIR = Path("/Users/bradfiles/Archive/Old Mac 2022 Files/Downloads")
REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "docs/workspaces/360-reviews/private/archive"
DB_PATH = OUT_DIR / "360-review-answers.sqlite"
WIDE_CSV = OUT_DIR / "360-review-answers-wide.csv"
PREFERRED_WIDE_CSV = OUT_DIR / "360-review-answers-preferred-wide.csv"
LONG_CSV = OUT_DIR / "360-review-answers-long.csv"
QUESTION_CATALOG_CSV = OUT_DIR / "360-review-question-catalog.csv"
NORMALIZED_RESPONSES_CSV = OUT_DIR / "360-review-responses-normalized.csv"
BROWSER_HTML = OUT_DIR / "browse.html"
README_PATH = OUT_DIR / "README.md"


FORM_FOOTER_MARKERS = [
    "Back            Submit",
    "Submit                                                                                Clear form",
    "Never submit passwords through Google Forms.",
    "This form was created inside of Northridge Church.",
    "Forms",
]


DEEP_GENERAL_QUESTIONS = [
    "Where does this person excel (or where have you seen this person excel in the last 6 months)?",
    "What improvements does this person need to make?",
    "What is this person doing that you think he/she should rethink, change or stop doing?",
    "What is this person NOT doing that you think he/she should START to do to make them more effective or their role more crucial?",
    "What might this person not know about him/herself that may be a blind spot?",
    "What does this person do better than just about anyone else on our team?",
]

WIDE_QUESTIONS = [
    "What do you appreciate most about what this person brings to our team?",
    "What skill or trait would you like to see this person work to improve?",
    "What is your overall perception of this person? (What 'vibe' do they give off?)",
]

DEEP_SCALE_SECTIONS = [
    (
        "CHARACTER",
        [
            "Doesn't make excuses, cover, or hide mistakes",
            "Hard working and self-motivated",
            "Humble, teachable, and anxious to learn",
            "Servant of others",
            "Represents our church and staff",
            "Overall Character",
        ],
    ),
    (
        "COMPETENCY",
        [
            "Completes responsibilities on time",
            "Completes responsibilities with excellence",
            "Brainstorms/develops options and ideas",
            "Plans ahead, anticipates obstacles & identifies solutions",
            "Helps us think strategically as a staff",
            "Overall Competency",
        ],
    ),
    (
        "COMMUNICATION & TEAMWORK",
        [
            "Listens to others in an active and attentive way",
            "Demonstrates effective written communication skills",
            "Demonstrates effective verbal communication skills",
            "This person is a true team player",
            "Manages and resolves conflict Biblically",
            "Overall Communication & Teamwork",
        ],
    ),
    (
        "WORK HABITS",
        [
            "Is prompt and prepared",
            "Demonstrates ability to set appropriate priorities",
            "Manages time well",
            "Demonstrates professionalism",
            "Overall Work Habits",
        ],
    ),
    (
        "GROWTH",
        [
            "A learner who seeks out answers/resources to get the job done",
            "Humbly seeks opportunities to serve outside of their specific job responsibilities",
            "Seeks opportunities to learn, outside of their specific job responsibilities",
            "Continually growing spiritually",
            "Lives a Pi2 lifestyle",
            "Overall Growth",
        ],
    ),
]

SCALE_LABELS = "Poor|Fair|Effective|Very Effective|Exceptional"


@dataclass
class Answer:
    number: int
    question: str
    answer: str


@dataclass
class Review:
    year: int
    name: str
    review_type: str
    source_path: str
    source_file: str
    source_format: str
    is_submitted: bool
    answers: list[Answer]


@dataclass
class FormQuestion:
    number: int
    section: str
    response_type: str
    question: str
    scale_labels: str = ""


def pdf_to_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.replace("\f", "\n")


def squash_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clean_answer(value: str) -> str:
    text = value.replace("\r", "\n")
    for marker in FORM_FOOTER_MARKERS:
        text = text.split(marker)[0]
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped in {
            "",
            "Clear selection",
            "Clear form",
            "Draft saved",
            "Not shared",
            "Switch account",
        }:
            continue
        if stripped == "Your answer":
            continue
        if stripped.startswith("bfiles@northridgerochester.com"):
            continue
        lines.append(stripped)
    return "\n".join(lines).strip()


def parse_filename(path: Path) -> tuple[int, str, str, bool]:
    match = re.match(r"Review-(?P<name>.+)-(?P<year>20\d{2})-(?P<rest>.+)\.pdf$", path.name)
    if not match:
        return 0, path.stem, "Unknown", False

    rest = match.group("rest")
    if "Wide" in rest:
        review_type = "Wide"
    elif "Deep" in rest:
        review_type = "Deep"
    elif "Part" in rest or "Self" in rest:
        review_type = "Self"
    else:
        review_type = "Unknown"

    name = match.group("name").replace("-", " ")
    return int(match.group("year")), name, review_type, "Submitted" in rest


NAME_ALIASES = {
    "Brad": "Brad Files",
    "Brit Catlin": "BrittJo Catlin",
    "Brit Jo Catlin": "BrittJo Catlin",
}


def normalize_name(name: str) -> str:
    cleaned = squash_spaces(name)
    return NAME_ALIASES.get(cleaned, cleaned)


def extract_evaluatee(text: str, fallback: str) -> str:
    marker = "Name of the Team Member you are evaluating"
    idx = text.find(marker)
    if idx == -1:
        return normalize_name(fallback)

    tail = text[idx + len(marker) :]
    for line in tail.splitlines():
        stripped = line.strip().strip("*")
        if not stripped:
            continue
        if stripped in {"CHARACTER", "COMPETENCY"}:
            break
        if stripped.startswith("Your Name"):
            continue
        return normalize_name(stripped)
    return normalize_name(fallback)


def find_answer_after(text: str, question_pattern: str, next_patterns: list[str]) -> str:
    match = re.search(question_pattern, text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
    if not match:
        return ""

    start = match.end()
    stops = []
    for pattern in next_patterns:
        stop = re.search(pattern, text[start:], flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
        if stop:
            stops.append(start + stop.start())
    end = min(stops) if stops else len(text)
    return clean_answer(text[start:end])


def extract_deep_answers(text: str) -> list[Answer]:
    answers: list[Answer] = []
    sections = ["CHARACTER", "COMPETENCY", "COMMUNICATION & TEAMWORK", "WORK HABITS", "GROWTH"]
    for section in sections:
        section_pattern = rf"{re.escape(section)}.*?Provide specific examples, details:\s*\*"
        next_patterns = [
            r"\n\s*CHARACTER\s*\n",
            r"\n\s*COMPETENCY\s*\n",
            r"\n\s*COMMUNICATION & TEAMWORK\s*\n",
            r"\n\s*WORK HABITS\s*\n",
            r"\n\s*GROWTH\s*\n",
            r"\n\s*GENERAL\s*\n",
        ]
        answer = find_answer_after(text, section_pattern, next_patterns)
        answers.append(Answer(len(answers) + 1, f"{section}: Provide specific examples, details", answer))

    normalized = re.sub(r"\s+", " ", text)
    for question in DEEP_GENERAL_QUESTIONS:
        q_pattern = re.escape(question)
        q_pattern = q_pattern.replace(r"\ ", r"\s+")
        next_patterns = []
        for next_question in DEEP_GENERAL_QUESTIONS:
            if next_question == question:
                continue
            next_pattern = re.escape(next_question).replace(r"\ ", r"\s+")
            next_patterns.append(next_pattern)
        next_patterns.extend([r"Back\s+Submit", r"Submit\s+Clear form", r"Never submit passwords"])
        answer = find_answer_after(normalized, q_pattern, next_patterns)
        answers.append(Answer(len(answers) + 1, question, answer))

    return answers


def extract_wide_answers(text: str) -> list[Answer]:
    normalized = re.sub(r"\s+", " ", text)
    answers: list[Answer] = []
    for question in WIDE_QUESTIONS:
        q_pattern = re.escape(question).replace(r"\ ", r"\s+")
        next_patterns = []
        for next_question in WIDE_QUESTIONS:
            if next_question == question:
                continue
            next_patterns.append(re.escape(next_question).replace(r"\ ", r"\s+"))
        next_patterns.extend([r"Submit\s+Clear form", r"Never submit passwords"])
        answer = find_answer_after(normalized, q_pattern, next_patterns)
        answers.append(Answer(len(answers) + 1, question, answer))
    return answers


def extract_self_answers(text: str) -> list[Answer]:
    # Self-assessments are less uniform, so capture numbered prompts conservatively.
    normalized = re.sub(r"\n\s+", "\n", text)
    pattern = re.compile(
        r"(?m)^(?P<num>\d+)\.\s+(?P<question>.+?\*)\s*\n(?P<answer>.*?)(?=^\d+\.\s+|\n[A-Z][A-Z ]+ QUESTIONS|\Z)",
        flags=re.DOTALL,
    )
    answers: list[Answer] = []
    for match in pattern.finditer(normalized):
        question = squash_spaces(match.group("question").rstrip("*"))
        answer = clean_answer(match.group("answer"))
        answers.append(Answer(len(answers) + 1, question, answer))
    return answers


def parse_pdf(path: Path) -> Review:
    year, filename_name, review_type, is_submitted = parse_filename(path)
    text = pdf_to_text(path)
    name = extract_evaluatee(text, filename_name) if review_type in {"Deep", "Wide"} else normalize_name(filename_name)

    if review_type == "Deep":
        answers = extract_deep_answers(text)
    elif review_type == "Wide":
        answers = extract_wide_answers(text)
    else:
        answers = extract_self_answers(text)

    return Review(
        year=year,
        name=name,
        review_type=review_type,
        source_path=str(path),
        source_file=path.name,
        source_format="pdf",
        is_submitted=is_submitted,
        answers=answers,
    )


def form_questions_for_review(review: Review) -> list[FormQuestion]:
    if review.review_type == "Deep":
        questions: list[FormQuestion] = []
        for section, scale_items in DEEP_SCALE_SECTIONS:
            for item in scale_items:
                questions.append(
                    FormQuestion(
                        number=len(questions) + 1,
                        section=section,
                        response_type="scale_1_5",
                        question=item,
                        scale_labels=SCALE_LABELS,
                    )
                )
            questions.append(
                FormQuestion(
                    number=len(questions) + 1,
                    section=section,
                    response_type="essay",
                    question=f"{section}: Provide specific examples, details",
                )
            )
        for question in DEEP_GENERAL_QUESTIONS:
            questions.append(
                FormQuestion(
                    number=len(questions) + 1,
                    section="GENERAL",
                    response_type="essay",
                    question=question,
                )
            )
        return questions

    if review.review_type == "Wide":
        return [
            FormQuestion(number=idx + 1, section="GENERAL", response_type="essay", question=question)
            for idx, question in enumerate(WIDE_QUESTIONS)
        ]

    return [
        FormQuestion(number=answer.number, section="SELF-ASSESSMENT", response_type="essay", question=answer.question)
        for answer in review.answers
    ]


def answer_for_question(review: Review, question: FormQuestion) -> str:
    if question.response_type.startswith("scale"):
        return ""
    answers_by_question = {answer.question: answer.answer for answer in review.answers}
    return answers_by_question.get(question.question, "")


def write_sqlite(reviews: list[Review]) -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        create table reviews (
            id integer primary key,
            year integer not null,
            name text not null,
            review_type text not null,
            source_path text not null,
            source_file text not null,
            source_format text not null,
            is_submitted integer not null
        )
        """
    )
    conn.execute(
        """
        create table answers (
            id integer primary key,
            review_id integer not null references reviews(id),
            question_number integer not null,
            question text not null,
            answer text not null
        )
        """
    )
    conn.execute(
        """
        create table preferred_reviews (
            review_id integer primary key references reviews(id)
        )
        """
    )
    conn.execute(
        """
        create table form_questions (
            id integer primary key,
            year integer not null,
            review_type text not null,
            question_number integer not null,
            section text not null,
            response_type text not null,
            question text not null,
            scale_labels text not null
        )
        """
    )
    conn.execute(
        """
        create table normalized_responses (
            id integer primary key,
            review_id integer not null references reviews(id),
            form_question_id integer not null references form_questions(id),
            answer text not null
        )
        """
    )

    review_ids: dict[int, int] = {}
    question_ids: dict[tuple[int, str, int, str, str], int] = {}
    for review in reviews:
        cursor = conn.execute(
            """
            insert into reviews (year, name, review_type, source_path, source_file, source_format, is_submitted)
            values (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review.year,
                review.name,
                review.review_type,
                review.source_path,
                review.source_file,
                review.source_format,
                int(review.is_submitted),
            ),
        )
        review_id = cursor.lastrowid
        review_ids[id(review)] = review_id
        conn.executemany(
            """
            insert into answers (review_id, question_number, question, answer)
            values (?, ?, ?, ?)
            """,
            [(review_id, answer.number, answer.question, answer.answer) for answer in review.answers],
        )

    conn.executemany(
        "insert into preferred_reviews (review_id) values (?)",
        [(review_ids[id(review)],) for review in preferred_reviews(reviews)],
    )

    for review in reviews:
        for question in form_questions_for_review(review):
            question_key = (
                review.year,
                review.review_type,
                question.number,
                question.response_type,
                question.question,
            )
            if question_key not in question_ids:
                cursor = conn.execute(
                    """
                    insert into form_questions (
                        year,
                        review_type,
                        question_number,
                        section,
                        response_type,
                        question,
                        scale_labels
                    )
                    values (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        review.year,
                        review.review_type,
                        question.number,
                        question.section,
                        question.response_type,
                        question.question,
                        question.scale_labels,
                    ),
                )
                question_ids[question_key] = cursor.lastrowid
            conn.execute(
                """
                insert into normalized_responses (review_id, form_question_id, answer)
                values (?, ?, ?)
                """,
                (
                    review_ids[id(review)],
                    question_ids[question_key],
                    answer_for_question(review, question),
                ),
            )

    conn.commit()
    conn.close()


def write_long_csv(reviews: list[Review]) -> None:
    with LONG_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "year",
                "name",
                "type",
                "source_file",
                "source_path",
                "is_submitted",
                "question_number",
                "question",
                "answer",
            ],
        )
        writer.writeheader()
        for review in reviews:
            for answer in review.answers:
                writer.writerow(
                    {
                        "year": review.year,
                        "name": review.name,
                        "type": review.review_type,
                        "source_file": review.source_file,
                        "source_path": review.source_path,
                        "is_submitted": review.is_submitted,
                        "question_number": answer.number,
                        "question": answer.question,
                        "answer": answer.answer,
                    }
                )


def write_wide_csv_to_path(reviews: list[Review], path: Path) -> None:
    max_answers = max((len(review.answers) for review in reviews), default=0)
    fieldnames = [
        "year",
        "name",
        "type",
        "source_file",
        "source_path",
        "is_submitted",
    ]
    for idx in range(1, max_answers + 1):
        fieldnames.extend([f"q{idx}_question", f"q{idx}_answer"])

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for review in reviews:
            row = {
                "year": review.year,
                "name": review.name,
                "type": review.review_type,
                "source_file": review.source_file,
                "source_path": review.source_path,
                "is_submitted": review.is_submitted,
            }
            for answer in review.answers:
                row[f"q{answer.number}_question"] = answer.question
                row[f"q{answer.number}_answer"] = answer.answer
            writer.writerow(row)


def write_wide_csv(reviews: list[Review]) -> None:
    write_wide_csv_to_path(reviews, WIDE_CSV)


def write_question_catalog_csv(reviews: list[Review]) -> None:
    seen: set[tuple[int, str, int, str, str]] = set()
    rows = []
    for review in reviews:
        for question in form_questions_for_review(review):
            key = (review.year, review.review_type, question.number, question.response_type, question.question)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "year": review.year,
                    "type": review.review_type,
                    "question_number": question.number,
                    "section": question.section,
                    "response_type": question.response_type,
                    "question": question.question,
                    "scale_labels": question.scale_labels,
                }
            )

    with QUESTION_CATALOG_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "year",
                "type",
                "question_number",
                "section",
                "response_type",
                "question",
                "scale_labels",
            ],
        )
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: (row["year"], row["type"], row["question_number"])))


def write_normalized_responses_csv(reviews: list[Review]) -> None:
    with NORMALIZED_RESPONSES_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "year",
                "name",
                "type",
                "source_file",
                "is_submitted",
                "question_number",
                "section",
                "response_type",
                "question",
                "scale_labels",
                "answer",
            ],
        )
        writer.writeheader()
        for review in reviews:
            for question in form_questions_for_review(review):
                writer.writerow(
                    {
                        "year": review.year,
                        "name": review.name,
                        "type": review.review_type,
                        "source_file": review.source_file,
                        "is_submitted": review.is_submitted,
                        "question_number": question.number,
                        "section": question.section,
                        "response_type": question.response_type,
                        "question": question.question,
                        "scale_labels": question.scale_labels,
                        "answer": answer_for_question(review, question),
                    }
                )


def write_browser_html(reviews: list[Review]) -> None:
    records = []
    question_records_by_key: dict[tuple[int, str, int], dict[str, object]] = {}
    for review in reviews:
        essay_answers = []
        for question in form_questions_for_review(review):
            question_records_by_key[(review.year, review.review_type, question.number)] = {
                "year": review.year,
                "type": review.review_type,
                "number": question.number,
                "section": question.section,
                "response_type": question.response_type,
                "question": question.question,
                "scale_labels": question.scale_labels,
            }
            if question.response_type != "essay":
                continue
            essay_answers.append(
                {
                    "number": question.number,
                    "section": question.section,
                    "question": question.question,
                    "answer": answer_for_question(review, question),
                }
            )
        records.append(
            {
                "year": review.year,
                "name": review.name,
                "type": review.review_type,
                "source_file": review.source_file,
                "source_path": review.source_path,
                "is_submitted": review.is_submitted,
                "answers": essay_answers,
            }
        )

    data_json = json.dumps(records, ensure_ascii=False)
    question_json = json.dumps(
        sorted(
            question_records_by_key.values(),
            key=lambda question: (question["year"], str(question["type"]), int(question["number"])),
        ),
        ensure_ascii=False,
    )
    favicon_href = f"""data:image/svg+xml,{quote('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#8c4f2b"/>
  <path d="M17 18h30v32H17z" fill="#fffdf8"/>
  <path d="M23 27h18M23 35h18M23 43h12" stroke="#536b45" stroke-width="4" stroke-linecap="round"/>
  <circle cx="47" cy="17" r="7" fill="#f0ddca"/>
  <text x="32" y="56" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#fffdf8">360</text>
</svg>''')}"""
    BROWSER_HTML.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Private 360 Review Browser</title>
  <link rel="icon" type="image/svg+xml" href="{favicon_href}">
  <style>
    :root {{
      --ink: #1e211c;
      --muted: #66705f;
      --paper: #fbf7ef;
      --card: #fffdf8;
      --line: #ded4c3;
      --accent: #8c4f2b;
      --accent-soft: #f0ddca;
      --green: #536b45;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top left, #f4d6b7 0, transparent 34rem),
        linear-gradient(135deg, #fbf7ef 0%, #f4eee1 55%, #e9ddcb 100%);
      color: var(--ink);
      font-family: Avenir Next, Charter, Georgia, serif;
      min-height: 100vh;
    }}
    header {{
      padding: 42px clamp(20px, 5vw, 72px) 22px;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(2.1rem, 5vw, 4.8rem);
      line-height: .92;
      letter-spacing: -0.055em;
      max-width: 980px;
    }}
    .lede {{
      color: var(--muted);
      font-size: 1.05rem;
      max-width: 760px;
      line-height: 1.6;
      margin-top: 18px;
    }}
    .shell {{
      display: grid;
      gap: 20px;
      grid-template-columns: minmax(260px, 340px) minmax(0, 1fr);
      padding: 0 clamp(20px, 5vw, 72px) 56px;
    }}
    aside, main {{
      background: color-mix(in srgb, var(--card) 88%, transparent);
      border: 1px solid var(--line);
      border-radius: 28px;
      box-shadow: 0 22px 70px rgba(67, 48, 28, .12);
    }}
    aside {{
      padding: 22px;
      align-self: start;
      position: sticky;
      top: 18px;
    }}
    main {{
      padding: 22px;
      min-height: 520px;
    }}
    label {{
      display: block;
      font-size: .72rem;
      font-weight: 800;
      letter-spacing: .12em;
      margin: 16px 0 8px;
      text-transform: uppercase;
      color: var(--green);
    }}
    select, input {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 12px 13px;
      background: #fffaf2;
      color: var(--ink);
      font: inherit;
    }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin: 0 0 18px;
    }}
    .stat {{
      background: var(--accent-soft);
      border-radius: 18px;
      padding: 13px;
    }}
    .stat strong {{
      display: block;
      font-size: 1.35rem;
      color: var(--accent);
    }}
    .stat span {{
      color: var(--muted);
      font-size: .78rem;
    }}
    .review {{
      border: 1px solid var(--line);
      background: #fffdf9;
      border-radius: 24px;
      margin: 0 0 16px;
      overflow: hidden;
    }}
    .review summary {{
      cursor: pointer;
      padding: 18px 20px;
      list-style: none;
      display: flex;
      gap: 12px;
      justify-content: space-between;
      align-items: center;
    }}
    .review summary::-webkit-details-marker {{ display: none; }}
    .title {{
      font-size: 1.16rem;
      font-weight: 800;
    }}
    .meta {{
      color: var(--muted);
      font-size: .88rem;
      margin-top: 4px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 7px 10px;
      background: var(--accent);
      color: #fffaf0;
      font-size: .76rem;
      font-weight: 800;
      letter-spacing: .06em;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .answers {{
      border-top: 1px solid var(--line);
      padding: 4px 20px 20px;
    }}
    .answer {{
      padding: 16px 0;
      border-bottom: 1px dashed #dfd1bd;
    }}
    .answer:last-child {{ border-bottom: 0; }}
    .question {{
      color: var(--green);
      font-weight: 800;
      margin-bottom: 8px;
    }}
    .response {{
      white-space: pre-wrap;
      line-height: 1.55;
    }}
    .empty {{
      color: var(--muted);
      font-style: italic;
    }}
    .matrix-section {{
      margin-bottom: 22px;
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 24px;
      background: #fffaf2;
    }}
    .matrix-head {{
      display: flex;
      justify-content: space-between;
      align-items: end;
      gap: 16px;
      margin-bottom: 14px;
    }}
    .matrix-head h2 {{
      margin: 0;
      font-size: clamp(1.3rem, 2.5vw, 2rem);
      letter-spacing: -0.045em;
    }}
    .matrix-head p {{
      margin: 6px 0 0;
      color: var(--muted);
      line-height: 1.5;
      max-width: 660px;
    }}
    .matrix-wrap {{
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 18px;
      background: #fffdf9;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 560px;
      font-family: Avenir Next, system-ui, sans-serif;
    }}
    th, td {{
      padding: 12px 14px;
      border-bottom: 1px solid #eadfce;
      text-align: left;
      vertical-align: middle;
      white-space: nowrap;
    }}
    th {{
      color: var(--green);
      background: #f3eadc;
      font-size: .78rem;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}
    tbody tr:last-child td {{
      border-bottom: 0;
    }}
    tbody tr:hover td {{
      background: #fff6e8;
    }}
    .person-cell {{
      font-weight: 800;
      color: var(--ink);
    }}
    .cell-types {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .type-chip {{
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 5px 9px;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--accent);
      font-size: .72rem;
      font-weight: 900;
      letter-spacing: .06em;
      text-transform: uppercase;
    }}
    .type-chip.deep {{ background: #e5eee0; color: #49663f; }}
    .type-chip.wide {{ background: #f3dfcf; color: #8c4f2b; }}
    .type-chip.self {{ background: #dfe8ed; color: #4d7286; }}
    button.type-chip {{
      border: 0;
      cursor: pointer;
      font: inherit;
    }}
    button.type-chip:hover {{
      transform: translateY(-1px);
      filter: saturate(1.18);
    }}
    .blank-cell {{
      color: #c3b59f;
    }}
    .question-browser {{
      margin-bottom: 22px;
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 24px;
      background: #fffaf2;
    }}
    .question-controls {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 220px)) minmax(180px, 1fr);
      gap: 12px;
      align-items: end;
      margin: 14px 0;
    }}
    .question-controls label {{
      margin-top: 0;
    }}
    .question-summary {{
      color: var(--muted);
      font-size: .92rem;
      line-height: 1.5;
    }}
    .question-list {{
      display: grid;
      gap: 8px;
      margin-top: 14px;
    }}
    .question-row {{
      display: grid;
      grid-template-columns: 56px 140px 110px minmax(0, 1fr);
      gap: 10px;
      align-items: start;
      padding: 12px;
      border: 1px solid #eadfce;
      border-radius: 16px;
      background: #fffdf9;
      font-family: Avenir Next, system-ui, sans-serif;
    }}
    .q-num {{
      color: var(--accent);
      font-weight: 900;
    }}
    .q-section {{
      color: var(--green);
      font-size: .78rem;
      font-weight: 900;
      letter-spacing: .06em;
      text-transform: uppercase;
    }}
    .q-type {{
      justify-self: start;
      border-radius: 999px;
      padding: 4px 8px;
      background: #efe5d6;
      color: var(--muted);
      font-size: .72rem;
      font-weight: 900;
      letter-spacing: .06em;
      text-transform: uppercase;
    }}
    .q-text {{
      line-height: 1.45;
    }}
    @media (max-width: 860px) {{
      .shell {{ grid-template-columns: 1fr; }}
      aside {{ position: static; }}
      .stats {{ grid-template-columns: 1fr; }}
      .matrix-head {{ align-items: flex-start; flex-direction: column; }}
      .question-controls, .question-row {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Private 360 Review Browser</h1>
    <p class="lede">A local-only view of past review answers, built from the private archive. Use this to compare years, people, Deep/Wide forms, and language patterns before writing 2026 reviews.</p>
  </header>
  <div class="shell">
    <aside>
      <div class="stats">
        <div class="stat"><strong id="visibleCount">0</strong><span>shown</span></div>
        <div class="stat"><strong id="answerCount">0</strong><span>answers</span></div>
        <div class="stat"><strong id="yearCount">0</strong><span>years</span></div>
      </div>
      <label for="year">Year</label>
      <select id="year"><option value="">All years</option></select>
      <label for="type">Type</label>
      <select id="type"><option value="">All types</option></select>
      <label for="person">Person</label>
      <select id="person"><option value="">All people</option></select>
      <label for="search">Search answers</label>
      <input id="search" placeholder="e.g. communication, leadership, growth">
    </aside>
    <main>
      <section class="matrix-section" aria-labelledby="matrixTitle">
        <div class="matrix-head">
          <div>
            <h2 id="matrixTitle">Review coverage matrix</h2>
            <p>Names down the left, years across the top. Each cell shows the review type found in the preferred archive.</p>
          </div>
        </div>
        <div id="coverageMatrix" class="matrix-wrap"></div>
      </section>
      <section class="question-browser" aria-labelledby="questionBrowserTitle">
        <div class="matrix-head">
          <div>
            <h2 id="questionBrowserTitle">Question browser</h2>
            <p>Browse the form structure by year and review type. Deep reaches 40 because it includes 29 rating prompts plus 11 essay prompts.</p>
          </div>
        </div>
        <div class="question-controls">
          <div>
            <label for="questionYear">Question year</label>
            <select id="questionYear"></select>
          </div>
          <div>
            <label for="questionType">Question type</label>
            <select id="questionType"></select>
          </div>
          <div id="questionSummary" class="question-summary"></div>
        </div>
        <div id="questionList" class="question-list"></div>
      </section>
      <section id="results" aria-label="Review answers"></section>
    </main>
  </div>
  <script>
    const reviews = {data_json};
    const questions = {question_json};
    const controls = {{
      year: document.querySelector("#year"),
      type: document.querySelector("#type"),
      person: document.querySelector("#person"),
      search: document.querySelector("#search"),
    }};
    const questionControls = {{
      year: document.querySelector("#questionYear"),
      type: document.querySelector("#questionType"),
    }};
    const results = document.querySelector("#results");
    const coverageMatrix = document.querySelector("#coverageMatrix");
    const questionList = document.querySelector("#questionList");
    const questionSummary = document.querySelector("#questionSummary");
    const visibleCount = document.querySelector("#visibleCount");
    const answerCount = document.querySelector("#answerCount");
    const yearCount = document.querySelector("#yearCount");
    const typeOrder = ["Deep", "Wide", "Self"];

    function optionize(select, values) {{
      for (const value of values) {{
        const option = document.createElement("option");
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
      }}
    }}

    optionize(controls.year, [...new Set(reviews.map(r => String(r.year)))].sort());
    optionize(controls.type, [...new Set(reviews.map(r => r.type))].sort());
    optionize(controls.person, [...new Set(reviews.map(r => r.name))].sort((a, b) => a.localeCompare(b)));
    optionize(questionControls.year, [...new Set(questions.map(q => String(q.year)))].sort());
    optionize(questionControls.type, [...new Set(questions.map(q => q.type))].sort());
    questionControls.year.value = questionControls.year.options[0]?.value || "";
    questionControls.type.value = questionControls.type.options[0]?.value || "";

    function reviewId(review) {{
      return `review-${{review.year}}-${{review.type}}-${{review.name}}-${{review.source_file}}`
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-|-$/g, "");
    }}

    function renderCoverageMatrix() {{
      const years = [...new Set(reviews.map(review => review.year))].sort();
      const names = [...new Set(reviews.map(review => review.name))].sort((a, b) => a.localeCompare(b));
      const coverage = new Map();

      for (const review of reviews) {{
        const key = `${{review.name}}::${{review.year}}`;
        if (!coverage.has(key)) coverage.set(key, new Set());
        coverage.get(key).add(review.type);
      }}

      const header = `
        <thead>
          <tr>
            <th>Person</th>
            ${{years.map(year => `<th>${{year}}</th>`).join("")}}
          </tr>
        </thead>
      `;

      const rows = names.map(name => `
        <tr>
          <td class="person-cell">${{name}}</td>
          ${{years.map(year => {{
            const types = coverage.get(`${{name}}::${{year}}`);
            if (!types) return '<td class="blank-cell">—</td>';
            const orderedTypes = typeOrder.filter(type => types.has(type));
            return `<td><div class="cell-types">${{orderedTypes.map(type => `<button class="type-chip ${{type.toLowerCase()}}" type="button" data-name="${{name}}" data-year="${{year}}" data-type="${{type}}">${{type}}</button>`).join("")}}</div></td>`;
          }}).join("")}}
        </tr>
      `).join("");

      coverageMatrix.innerHTML = `<table>${{header}}<tbody>${{rows}}</tbody></table>`;

      coverageMatrix.querySelectorAll(".type-chip").forEach(button => {{
        button.addEventListener("click", () => jumpToReview(button.dataset.name, button.dataset.year, button.dataset.type));
      }});
    }}

    function renderQuestionBrowser() {{
      const selectedYear = questionControls.year.value;
      const selectedType = questionControls.type.value;
      const filtered = questions.filter(question => String(question.year) === selectedYear && question.type === selectedType);
      const scaleCount = filtered.filter(question => question.response_type === "scale_1_5").length;
      const essayCount = filtered.filter(question => question.response_type === "essay").length;

      questionSummary.textContent = `${{filtered.length}} total prompts: ${{scaleCount}} rating prompts and ${{essayCount}} essay prompts.`;
      questionList.innerHTML = filtered.map(question => `
        <section class="question-row">
          <div class="q-num">Q${{question.number}}</div>
          <div class="q-section">${{question.section}}</div>
          <div class="q-type">${{question.response_type === "scale_1_5" ? "rating" : "essay"}}</div>
          <div class="q-text">${{question.question}}</div>
        </section>
      `).join("");
    }}

    function matches(review) {{
      const q = controls.search.value.trim().toLowerCase();
      if (controls.year.value && String(review.year) !== controls.year.value) return false;
      if (controls.type.value && review.type !== controls.type.value) return false;
      if (controls.person.value && review.name !== controls.person.value) return false;
      if (!q) return true;
      const haystack = [
        review.year,
        review.name,
        review.type,
        review.source_file,
        ...review.answers.flatMap(answer => [answer.section, answer.question, answer.answer]),
      ].join(" ").toLowerCase();
      return haystack.includes(q);
    }}

    function render() {{
      const filtered = reviews.filter(matches);
      visibleCount.textContent = filtered.length;
      answerCount.textContent = filtered.reduce((sum, review) => sum + review.answers.length, 0);
      yearCount.textContent = new Set(filtered.map(review => review.year)).size;
      results.innerHTML = "";

      if (!filtered.length) {{
        results.innerHTML = '<p class="empty">No matching reviews. Try broadening the filters.</p>';
        return;
      }}

      for (const review of filtered) {{
        const details = document.createElement("details");
        details.className = "review";
        details.id = reviewId(review);
        details.open = filtered.length <= 4;
        details.innerHTML = `
          <summary>
            <div>
              <div class="title">${{review.name}}</div>
              <div class="meta">${{review.year}} • ${{review.type}} • ${{review.source_file}}</div>
            </div>
            <span class="pill">${{review.is_submitted ? "submitted" : "draft/source"}}</span>
          </summary>
          <div class="answers">
            ${{review.answers.map(answer => `
              <section class="answer">
                <div class="question">${{answer.section}} · Q${{answer.number}} · ${{answer.question}}</div>
                <div class="response">${{answer.answer || '<span class="empty">No answer extracted.</span>'}}</div>
              </section>
            `).join("")}}
          </div>
        `;
        results.appendChild(details);
      }}
    }}

    function jumpToReview(name, year, type) {{
      controls.search.value = "";
      controls.person.value = name;
      controls.year.value = String(year);
      controls.type.value = type;
      render();
      const review = reviews.find(item => item.name === name && String(item.year) === String(year) && item.type === type);
      if (!review) return;
      const element = document.getElementById(reviewId(review));
      if (!element) return;
      element.open = true;
      element.scrollIntoView({{ behavior: "smooth", block: "start" }});
    }}

    for (const control of Object.values(controls)) {{
      control.addEventListener("input", render);
    }}
    for (const control of Object.values(questionControls)) {{
      control.addEventListener("input", renderQuestionBrowser);
    }}
    renderCoverageMatrix();
    renderQuestionBrowser();
    render();
  </script>
</body>
</html>
""",
        encoding="utf-8",
    )


def source_group_key(review: Review) -> tuple[int, str, str, str]:
    match = re.match(r"Review-(?P<slug>.+)-(?P<year>20\d{2})-(?P<rest>.+)\.pdf$", review.source_file)
    if not match:
        return (review.year, review.review_type, review.name.lower(), review.source_file.lower())
    slug = re.sub(r"[^a-z0-9]+", "", match.group("slug").lower())
    rest = match.group("rest").lower()
    subtype = "self" if "self" in rest or "part" in rest else "standard"
    return (review.year, review.review_type, slug, subtype)


def preferred_reviews(reviews: list[Review]) -> list[Review]:
    grouped: dict[tuple[int, str, str, str], list[Review]] = {}
    for review in reviews:
        grouped.setdefault(source_group_key(review), []).append(review)

    selected = []
    for group in grouped.values():
        selected.append(
            sorted(
                group,
                key=lambda review: (
                    not review.is_submitted,
                    "(1)" in review.source_file,
                    len(review.source_file),
                    review.source_file,
                ),
            )[0]
        )
    return sorted(selected, key=lambda review: (review.year, review.review_type, review.name, review.source_file))


def write_readme(total_reviews: int, preferred_count: int) -> None:
    README_PATH.write_text(
        f"""# Private 360 Review Archive

Generated from local review PDFs using filename matching and `pdftotext`.

Generator:

- `tools/360/build-review-archive.py`

Generated files:

- `360-review-answers.sqlite`: queryable SQLite database with `reviews`, `answers`, and `preferred_reviews`.
- `360-review-answers-wide.csv`: one row per source PDF, with `q1_question`, `q1_answer`, etc.
- `360-review-answers-long.csv`: one row per answer, useful for filtering by question.
- `360-review-answers-preferred-wide.csv`: one row per preferred review source, preferring submitted PDFs when duplicate draft/submitted versions exist.
- `360-review-question-catalog.csv`: one row per question asked by year and review type, including scale prompts.
- `360-review-responses-normalized.csv`: one row per review/question pair for trend analysis.
- `browse.html`: private static browser for filtering by year, person, type, and search term.

Current counts:

- Source PDFs archived: {total_reviews}
- Preferred review rows: {preferred_count}

Privacy:

- This folder is ignored by git.
- The archive contains HR review content and should stay private unless Brad intentionally changes that boundary.
- The generator code is tracked separately because it is not confidential; only the generated review content is private.
- The builder reads local PDF contents but does not modify the source PDFs.

Notes:

- Deep review scale prompts are archived as `scale_1_5` with labels `Poor`, `Fair`, `Effective`, `Very Effective`, and `Exceptional`.
- The PDFs do not reliably expose which radio-button scale value was selected, so scale answers are blank unless a better export source is found later.
- Essay answers are extracted from the local PDFs.
""",
        encoding="utf-8",
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_paths = sorted(Path(path) for path in glob.glob(str(SOURCE_DIR / "Review-*.pdf")))
    reviews = [parse_pdf(path) for path in pdf_paths]
    preferred = preferred_reviews(reviews)

    write_sqlite(reviews)
    write_long_csv(reviews)
    write_wide_csv(reviews)
    write_wide_csv_to_path(preferred, PREFERRED_WIDE_CSV)
    write_question_catalog_csv(reviews)
    write_normalized_responses_csv(reviews)
    write_browser_html(preferred)
    write_readme(len(reviews), len(preferred))

    print(f"Archived {len(reviews)} review PDFs.")
    print(f"Selected {len(preferred)} preferred review rows.")
    print(f"Wrote {DB_PATH}")
    print(f"Wrote {LONG_CSV}")
    print(f"Wrote {WIDE_CSV}")
    print(f"Wrote {PREFERRED_WIDE_CSV}")
    print(f"Wrote {QUESTION_CATALOG_CSV}")
    print(f"Wrote {NORMALIZED_RESPONSES_CSV}")
    print(f"Wrote {BROWSER_HTML}")
    print(f"Wrote {README_PATH}")


if __name__ == "__main__":
    main()
