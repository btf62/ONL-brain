import argparse
import csv
import json
from pathlib import Path
from typing import Any, Optional

from todoist_client import TodoistClient, TodoistError


EXPORT_FIELDNAMES = [
    "Task ID",
    "Task Name",
    "Due Date",
    "Due Time",
    "Created At",
    "Completed At",
    "Priority",
    "Todoist Priority",
    "Project ID",
    "Project Name",
    "Project Parent ID",
    "Project Parent Name",
    "Labels",
    "Description",
    "Order",
    "Parent Task ID",
    "Parent Task Name",
    "URL",
    "Section ID",
    "Section Name",
    "Completed Status",
    "Task Comment Count",
    "Task Recurrence",
]


def todoist_priority_label(api_priority: Any) -> str:
    # Todoist's API uses 4 for the client-facing P1 / highest priority.
    return {
        4: "P1",
        3: "P2",
        2: "P3",
        1: "P4",
    }.get(api_priority, "")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Small Todoist CLI for export, inspection, creation, and updates."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser(
        "export", help="Export active Todoist tasks to a CSV file."
    )
    export_parser.add_argument(
        "--output",
        default="data/todoist_tasks_with_parents.csv",
        help="Output CSV path. Defaults to data/todoist_tasks_with_parents.csv",
    )

    get_task_parser = subparsers.add_parser(
        "get-task", help="Print the raw JSON for a single Todoist task."
    )
    get_task_parser.add_argument("task_id", help="Todoist task ID")

    create_task_parser = subparsers.add_parser(
        "create-task", help="Create a new Todoist task."
    )
    create_task_parser.add_argument("content", help="Task content")
    create_task_parser.add_argument("--description", help="Task description")
    create_task_parser.add_argument("--project-id", help="Todoist project ID")
    create_task_parser.add_argument("--section-id", help="Todoist section ID")
    create_task_parser.add_argument("--parent-id", help="Parent task ID")
    create_task_parser.add_argument("--priority", type=int, help="Priority value to send")
    create_task_parser.add_argument("--due-date", help="Due date in YYYY-MM-DD format")
    create_task_parser.add_argument(
        "--due-string", help='Natural-language due string like "tomorrow at 9am"'
    )
    create_task_parser.add_argument(
        "--labels",
        help="Comma-separated labels, for example onl,operations,follow-up",
    )

    update_priority_parser = subparsers.add_parser(
        "update-priority", help="Bulk-update tasks from one priority to another."
    )
    update_priority_parser.add_argument("source_priority", type=int)
    update_priority_parser.add_argument("destination_priority", type=int)
    update_priority_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show matching tasks without changing anything.",
    )

    return parser


def build_export_rows(
    tasks: list[dict[str, Any]],
    projects: list[dict[str, Any]],
    sections: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    project_dict = {project["id"]: project for project in projects}
    section_dict = {section["id"]: section["name"] for section in sections}
    task_dict = {task["id"]: task["content"] for task in tasks}

    rows = []
    for task in tasks:
        project = project_dict.get(task.get("project_id"), {})
        project_parent_id = project.get("parent_id", "")
        rows.append(
            {
                "Task ID": task.get("id", ""),
                "Task Name": task.get("content", ""),
                "Due Date": task.get("due", {}).get("date", "") if task.get("due") else "",
                "Due Time": task.get("due", {}).get("datetime", "")
                if task.get("due")
                else "",
                "Created At": task.get("created_at") or task.get("added_at", ""),
                "Completed At": "",
                "Priority": task.get("priority", ""),
                "Todoist Priority": todoist_priority_label(task.get("priority")),
                "Project ID": task.get("project_id", ""),
                "Project Name": project.get("name", ""),
                "Project Parent ID": project_parent_id,
                "Project Parent Name": project_dict.get(project_parent_id, {}).get(
                    "name", ""
                ),
                "Labels": ", ".join(task.get("labels", [])),
                "Description": task.get("description", ""),
                "Order": task.get("order", ""),
                "Parent Task ID": task.get("parent_id", ""),
                "Parent Task Name": task_dict.get(task.get("parent_id"), "")
                if task.get("parent_id")
                else "",
                "URL": task.get("url", ""),
                "Section ID": task.get("section_id", ""),
                "Section Name": section_dict.get(task.get("section_id"), "")
                if task.get("section_id")
                else "",
                "Completed Status": task.get("is_completed", False),
                "Task Comment Count": task.get("comment_count", task.get("note_count", "")),
                "Task Recurrence": task.get("due", {}).get("recurring", False)
                if task.get("due")
                else "",
            }
        )
    return rows


def export_tasks(client: TodoistClient, output_path: str) -> None:
    tasks = client.get_tasks()
    projects = client.get_projects()
    sections = client.get_sections()
    rows = build_export_rows(tasks, projects, sections)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=EXPORT_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} tasks to {output}")


def print_task(task: dict[str, Any]) -> None:
    print(json.dumps(task, indent=2, sort_keys=True))


def parse_labels(raw_labels: Optional[str]) -> Optional[list[str]]:
    if not raw_labels:
        return None
    labels = [label.strip() for label in raw_labels.split(",")]
    return [label for label in labels if label]


def create_task(client: TodoistClient, args: argparse.Namespace) -> None:
    task = client.create_task(
        content=args.content,
        description=args.description,
        project_id=args.project_id,
        section_id=args.section_id,
        parent_id=args.parent_id,
        priority=args.priority,
        due_date=args.due_date,
        due_string=args.due_string,
        labels=parse_labels(args.labels),
    )
    print_task(task)


def update_priority(client: TodoistClient, args: argparse.Namespace) -> None:
    tasks = client.get_tasks()
    matching_tasks = [
        task for task in tasks if task.get("priority", 1) == args.source_priority
    ]

    if not matching_tasks:
        print(f"No tasks found with priority {args.source_priority}.")
        return

    for task in matching_tasks:
        if args.dry_run:
            print(
                f"[DRY RUN] Would update task {task['id']} "
                f"'{task.get('content', '')}' to priority {args.destination_priority}"
            )
            continue

        client.update_task_priority(task["id"], args.destination_priority)
        print(
            f"Updated task {task['id']} "
            f"'{task.get('content', '')}' to priority {args.destination_priority}"
        )

    print(f"Matched {len(matching_tasks)} task(s).")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        client = TodoistClient()

        if args.command == "export":
            export_tasks(client, args.output)
        elif args.command == "get-task":
            print_task(client.get_task(args.task_id))
        elif args.command == "create-task":
            create_task(client, args)
        elif args.command == "update-priority":
            update_priority(client, args)
        else:
            parser.error(f"Unknown command: {args.command}")
    except TodoistError as exc:
        print(f"Error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
