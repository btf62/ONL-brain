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
11. [Online Analytics Reporting](docs/operations/analytics-reporting.md)
12. [Online Analytics Toolkit](tools/analytics/README.md)

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
- `docs/operations/analytics-reporting.md` defines the weekly online analytics reporting responsibility for numbers sent to `jennie.miller@northridgerochester.com`.
- `docs/dashboards/online-analytics-metrics.md` defines the first-pass metric model for Church Online Platform, Resi, YouTube, Facebook, and app/TV analytics.
- `tools/analytics/` contains the starter online analytics CLI for creating, validating, and summarizing weekly JSON records.
- `agents/personal/cbt-coach.md` defines the personal effectiveness support posture.
- `agents/ministry/` defines task-specific ministry support agents.

## Current stopping point: online analytics

An online analytics reporting domain has been added but not yet run against a real week.

Current shape:

- [Online Analytics Reporting](docs/operations/analytics-reporting.md) names the responsibility, weekly workflow, source map, Jennie reporting boundary, and automation roadmap.
- [Online Analytics Metrics](docs/dashboards/online-analytics-metrics.md) defines source metrics, normalized weekly fields, confidence levels, and data-quality flags.
- [Online Analytics Reporting Agent](agents/ministry/online-analytics-reporting-agent.md) defines the agent role that prepares analytics summaries without sending email.
- [Online Analytics Toolkit](tools/analytics/README.md) and `tools/analytics/analytics_cli.py` create weekly JSON records, validate missing data, and print a draft report.
- [Source Systems](docs/governance/source-systems.md) now includes Church Online Platform, Resi, YouTube, Facebook/Meta, and Triumph/app/TV boundaries.

Key vendor findings from public docs:

- Church Online Platform has admin analytics for attendance, unique viewers, peak concurrent, chat, prayer, and Moments, but no public reporting API has been confirmed.
- Resi publicly documents analytics, exports, Facebook social analytics, and a Go Live API; public analytics API access has not been confirmed.
- YouTube is the strongest first API candidate through the official YouTube Analytics API using read-only OAuth scopes.
- Facebook/Meta may be possible through Page/Business Suite or Graph API, but permissions and Page/video/live metric definitions need careful testing.

Recommended next session:

1. Ask Brad what exact fields Jennie currently expects and what deadline/channel she uses.
2. Create one real weekly analytics JSON record with `python3 tools/analytics/analytics_cli.py new-week --week-start YYYY-MM-DD --output data/online-analytics/YYYY-MM-DD.json`.
3. Manually collect one week from Church Online Platform, Resi, YouTube, and Facebook/app sources as available.
4. Run `validate` and `summarize`; use the missing-source warnings to decide which source should be automated first.
5. Most likely first automation: YouTube Analytics read-only connector; likely second: Resi export parser.

## Context caveat

This file is a restoration map, not a full memory dump. A new session should still inspect the current git status, recent commits, and relevant docs before acting.

Useful commands:

```bash
git status --short --ignored
git log --oneline -5
rg --files -g '*.md'
```
