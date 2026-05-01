# 360 Reviews Workspace

This workspace supports annual 360 review work without committing confidential personnel-review content.

## Purpose

- collect non-confidential instructions
- name the annual review workflow
- keep current-year review work from becoming one vague overwhelming task
- provide a place to reference past inputs privately

## Current known 2026 items

- 360 self-assessment kickoff email was sent April 9, 2026.
- Self-assessment was due April 16, 2026.
- Annual Staff Requirements are due April 30, 2026.
- Deep & Wide review activity is expected around May 1, 2026.

## 2025 reference pattern

- Self-assessment reminder came before Deep & Wide assignments.
- Deep & Wide assignments were sent May 2, 2025.
- Assignments were due May 16, 2025.
- Brad completed the assigned reviews by May 16/17, 2025.
- Review conversation information arrived June 9, 2025.

## Private archive

Use this local ignored folder for sensitive material:

- `docs/workspaces/360-reviews/private/`

This folder is ignored by git.

It may hold:

- past review inputs
- current-year draft language
- employee-specific notes
- private writing prompts

The archive builder code is tracked at:

- `tools/360/build-review-archive.py`

That script generates private archive outputs under:

- `docs/workspaces/360-reviews/private/archive/`

Keep the generated content private, but keep the reusable code outside `private/`.

Do not commit:

- employee-specific review content
- confidential review drafts
- personally sensitive performance feedback
- final submitted review text unless intentionally sanitized

## Suggested local private files

These are examples for the ignored `private/` folder:

- `2025-past-inputs.md`
- `2026-self-assessment-draft.md`
- `2026-deep-reviews-draft.md`
- `2026-wide-reviews-draft.md`
- `review-language-bank.md`

## Writing approach

Use one small batch at a time:

1. Gather the assigned names privately.
2. Create a short note for each person.
3. Write strengths before concerns.
4. Name one concrete example where possible.
5. Keep tone truthful, kind, and useful.
6. Submit one review at a time.

## Repo boundary

The repo may store:

- workflow
- checklist
- non-confidential timeline
- source email references
- privacy rules

The repo should not store:

- confidential HR feedback
- named employee-review drafts
- private performance notes

## Private calibration guidance

The private file `docs/workspaces/360-reviews/private/2026-review-writing-guidance.md` captures the 2026 task list, prior-year form links, and Deep review rating guidance.

Key calibration rule: `3 / Effective` is the normal positive rating where most of the team should land; `4 / Very Effective` is top 25% in that area; `5 / Exceptional` is top 5% in that area.
