# Todoist Toolkit

This folder contains a small Todoist CLI based on the patterns in the older standalone scripts.

## What changed

- Uses `TODOIST_API_TOKEN` from the environment instead of hard-coded tokens
- Shares one client instead of repeating API logic across scripts
- Drops the `pandas` dependency and exports plain CSV
- Adds create and inspect commands alongside export and priority updates

## Setup

Set your Todoist API token in the shell before running commands:

```bash
export TODOIST_API_TOKEN="your-token-here"
```

## Commands

Show help:

```bash
python3 tools/todoist/todoist_cli.py --help
```

Export tasks to CSV:

```bash
python3 tools/todoist/todoist_cli.py export
```

Export tasks to a custom path:

```bash
python3 tools/todoist/todoist_cli.py export --output /tmp/todoist.csv
```

Inspect one task:

```bash
python3 tools/todoist/todoist_cli.py get-task 1234567890
```

Create a task:

```bash
python3 tools/todoist/todoist_cli.py create-task "Review ONL dashboard metrics" \
  --description "Use weekly scorecard and update Confluence summary" \
  --priority 3 \
  --labels onl,operations
```

Bulk-update priorities without changing anything:

```bash
python3 tools/todoist/todoist_cli.py update-priority 1 2 --dry-run
```

Bulk-update priorities for real:

```bash
python3 tools/todoist/todoist_cli.py update-priority 1 2
```

## Notes

- Priority values are passed through directly to the Todoist REST API.
- The export currently targets active tasks, matching the older scripts.
- If we want to grow this further, the next sensible additions are project listing, section listing, and task completion or close-out commands.
