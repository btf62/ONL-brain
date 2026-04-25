# Session Handoff

Use this file to restore working context in a new Codex session.

## Restore prompt

Shortest sufficient prompt:

```text
Read HANDOFF.md before doing any work, then follow it.
```

Suggested prompt:

```text
We are in /Users/bradfiles/Code/ONL-brain. Read AGENTS.md, README.md, and HANDOFF.md first, then follow the linked overview/governance docs before doing any work. Pay special attention to access-and-safety.md, source-systems.md, agents/README.md, and the active workspace/tool READMEs.
```

Short VS Code/Codex prompt:

```text
We are in /Users/bradfiles/Code/ONL-brain. Read AGENTS.md, README.md, and HANDOFF.md before doing any work, then follow any linked safety and governance docs relevant to the task.
```

If the task involves sensitive systems, also say:

```text
Use narrow reads only. Do not send email except an explicitly requested self-email to bfiles@northridgerochester.com. Do not create, update, delete, RSVP to, or schedule calendar events. Treat Todoist as read-only unless I explicitly ask for a specific write.
```

## First files to read

Read in this order:

1. [AGENTS.md](AGENTS.md)
2. [README.md](README.md)
3. [HANDOFF.md](HANDOFF.md)
4. [Access and Safety](docs/governance/access-and-safety.md)
5. [Source Systems](docs/governance/source-systems.md)
6. [Agents Overview](agents/README.md)
7. [Governance Overview](docs/governance/README.md)
8. [Dashboards Overview](docs/dashboards/README.md)
9. [360 Reviews Workspace](docs/workspaces/360-reviews/README.md)
10. [Todoist Toolkit](tools/todoist/README.md)

Then read the area-specific docs for the task at hand.

## Current repo purpose

`ONL-brain` is the operating system for Brad's online campus pastor role. It captures the durable structure around vision, operations, people, roles, dashboards, source systems, agents, and private workspaces.

The repo is not meant to replace Rock RMS, Google Drive, Gmail, Google Calendar, Todoist, Confluence, ScriptBrain, Rock Agent, or Rock Workbench. It names how those systems relate to the work and stores the structured operating knowledge that should survive across sessions.

## Current safety posture

- Access does not imply permission to browse.
- Gmail and Google Calendar reads must stay narrow and user-requested.
- Gmail may send only to `bfiles@northridgerochester.com`, and only when Brad explicitly requests a self-email.
- Google Calendar is strictly read-only: no create, update, delete, RSVP, invite, or scheduling actions.
- Todoist tools may expose writes, but the working posture is read-only unless Brad explicitly requests a specific write.
- HR/360 review content belongs in `docs/workspaces/360-reviews/private/`, which is git-ignored.
- Do not commit private review content, secrets, `.env`, or unnecessary sensitive pastoral/staff details.

## Important active areas

- `docs/dashboards/repo-map.html` gives a browser-friendly map of the repo.
- `docs/dashboards/onl-brain-overview.html` gives a visual overview of the scope of work.
- `docs/workspaces/360-reviews/` documents the public 360 workflow; private archive content stays ignored.
- `tools/todoist/` contains the Todoist CLI and client.
- `agents/personal/cbt-coach.md` defines the personal effectiveness support posture.
- `agents/ministry/` defines task-specific ministry support agents.

## Context caveat

This file is a restoration map, not a full memory dump. A new session should still inspect the current git status, recent commits, and relevant docs before acting.

Useful commands:

```bash
git status --short --ignored
git log --oneline -5
rg --files -g '*.md'
```
