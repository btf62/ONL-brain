#!/usr/bin/env python3
"""Small helpers for weekly online analytics reporting."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_RECIPIENT = "jennie.miller@northridgerochester.com"

SOURCE_TEMPLATES: dict[str, dict[str, Any]] = {
    "church_online_platform": {
        "status": "pending",
        "collection_method": "manual_ui",
        "confidence": "manual_ui",
        "metrics": {
            "attendance": None,
            "unique_viewers": None,
            "peak_concurrent": None,
            "average_time_attended_minutes": None,
            "public_chat_participants": None,
            "public_chat_messages": None,
            "prayer_requests": None,
            "prayer_sessions": None,
            "moment_interactions": None,
        },
        "notes": "",
    },
    "resi": {
        "status": "pending",
        "collection_method": "manual_export",
        "confidence": "manual_ui",
        "metrics": {
            "live_viewers": None,
            "live_views": None,
            "peak_concurrent": None,
            "average_watch_time_minutes": None,
            "total_watch_time_minutes": None,
            "on_demand_views": None,
            "facebook_views": None,
        },
        "notes": "",
    },
    "youtube": {
        "status": "pending",
        "collection_method": "manual_ui",
        "confidence": "manual_ui",
        "metrics": {
            "views": None,
            "estimated_minutes_watched": None,
            "average_view_duration_seconds": None,
            "peak_concurrent_viewers": None,
            "average_concurrent_viewers": None,
            "video_id": "",
            "channel_id": "",
        },
        "notes": "",
    },
    "facebook": {
        "status": "pending",
        "collection_method": "manual_ui",
        "confidence": "unknown",
        "metrics": {
            "video_views": None,
            "minutes_viewed": None,
            "three_second_views": None,
            "reactions": None,
            "comments": None,
            "shares": None,
            "video_or_post_id": "",
        },
        "notes": "",
    },
    "app_tv": {
        "status": "pending",
        "collection_method": "unknown",
        "confidence": "unknown",
        "metrics": {
            "mobile_app_views": None,
            "apple_tv_views": None,
            "roku_views": None,
            "source_system": "",
        },
        "notes": "",
    },
}


def parse_date(value: str) -> str:
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc
    return parsed.isoformat()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("weekly analytics file must contain a JSON object")
    return data


def write_json(path: Path, data: dict[str, Any], force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; use --force to overwrite")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def new_week(args: argparse.Namespace) -> int:
    week_start = args.week_start
    created_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    data = {
        "week_start": week_start,
        "service_date": "",
        "service_label": "",
        "report_recipient": DEFAULT_RECIPIENT,
        "created_at": created_at,
        "updated_at": created_at,
        "sources": SOURCE_TEMPLATES,
        "normalized_report": {
            "headline_online_attendance": None,
            "headline_online_attendance_method": "",
            "total_known_platform_views": None,
            "total_known_platform_views_method": "",
            "methodology_notes": [],
            "missing_sources": [],
            "data_quality_flags": [],
        },
        "draft_notes_for_jennie": [],
    }
    write_json(args.output, data, args.force)
    print(f"Created {args.output}")
    return 0


def validate_data(data: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    for key in ("week_start", "report_recipient", "sources", "normalized_report"):
        if key not in data:
            warnings.append(f"missing required key: {key}")

    sources = data.get("sources", {})
    if not isinstance(sources, dict):
        warnings.append("sources must be an object")
        return warnings

    for source_name in SOURCE_TEMPLATES:
        source = sources.get(source_name)
        if source is None:
            warnings.append(f"missing source: {source_name}")
            continue
        if not isinstance(source, dict):
            warnings.append(f"source {source_name} must be an object")
            continue
        if source.get("status") == "pending":
            warnings.append(f"source still pending: {source_name}")
        if source.get("confidence") in ("unknown", None, ""):
            warnings.append(f"source confidence unknown: {source_name}")

    normalized = data.get("normalized_report", {})
    if isinstance(normalized, dict):
        if normalized.get("headline_online_attendance") is None:
            warnings.append("headline_online_attendance is blank")
        if normalized.get("total_known_platform_views") is None:
            warnings.append("total_known_platform_views is blank")
    else:
        warnings.append("normalized_report must be an object")

    return warnings


def validate(args: argparse.Namespace) -> int:
    data = load_json(args.input)
    warnings = validate_data(data)
    if not warnings:
        print("OK")
        return 0
    for warning in warnings:
        print(f"WARN: {warning}")
    return 1 if args.strict else 0


def format_value(value: Any) -> str:
    if value in (None, ""):
        return "blank"
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)


def summarize(args: argparse.Namespace) -> int:
    data = load_json(args.input)
    normalized = data.get("normalized_report", {})
    print(f"Online analytics draft for week of {data.get('week_start', 'unknown')}")
    if data.get("service_label"):
        print(f"Service: {data['service_label']}")
    if data.get("service_date"):
        print(f"Service date: {data['service_date']}")
    print(f"Report recipient: {data.get('report_recipient', DEFAULT_RECIPIENT)}")
    print()

    print("Headline")
    print(f"- Online attendance: {format_value(normalized.get('headline_online_attendance'))}")
    if normalized.get("headline_online_attendance_method"):
        print(f"- Attendance method: {normalized['headline_online_attendance_method']}")
    print(f"- Known platform views: {format_value(normalized.get('total_known_platform_views'))}")
    if normalized.get("total_known_platform_views_method"):
        print(f"- Views method: {normalized['total_known_platform_views_method']}")
    print()

    print("Sources")
    sources = data.get("sources", {})
    for source_name, source in sources.items():
        if not isinstance(source, dict):
            continue
        status = source.get("status", "unknown")
        confidence = source.get("confidence", "unknown")
        print(f"- {source_name}: {status}, confidence={confidence}")
        metrics = source.get("metrics", {})
        if isinstance(metrics, dict):
            filled = {key: value for key, value in metrics.items() if value not in (None, "")}
            for key, value in filled.items():
                print(f"  - {key}: {format_value(value)}")
        if source.get("notes"):
            print(f"  - notes: {source['notes']}")
    print()

    notes = data.get("draft_notes_for_jennie", [])
    if notes:
        print("Notes for Jennie")
        for note in notes:
            print(f"- {note}")
        print()

    warnings = validate_data(data)
    if warnings:
        print("Data quality")
        for warning in warnings:
            print(f"- {warning}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Online analytics reporting helpers")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_week_parser = subparsers.add_parser("new-week", help="create a weekly JSON record")
    new_week_parser.add_argument("--week-start", required=True, type=parse_date)
    new_week_parser.add_argument("--output", required=True, type=Path)
    new_week_parser.add_argument("--force", action="store_true")
    new_week_parser.set_defaults(func=new_week)

    validate_parser = subparsers.add_parser("validate", help="validate a weekly JSON record")
    validate_parser.add_argument("input", type=Path)
    validate_parser.add_argument("--strict", action="store_true")
    validate_parser.set_defaults(func=validate)

    summarize_parser = subparsers.add_parser("summarize", help="print a draft report")
    summarize_parser.add_argument("input", type=Path)
    summarize_parser.set_defaults(func=summarize)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
