# Session Health

This document defines the lightweight startup and context-check pattern for ONL Brain sessions.

ONL Brain is an operations-knowledge and continuity domain. Its health checks should protect privacy, preserve current handoffs, and make connector use intentional.

## Shorthand Prompts

Use these prompts consistently in this repo.

### `Read README`

Bootstrap the session by reading:

1. [README.md](../../README.md)
2. [AGENTS.md](../../AGENTS.md)
3. [HANDOFF.md](../../HANDOFF.md)
4. [Access and Safety](access-and-safety.md)
5. [Source Systems](source-systems.md)
6. this file when the task involves context checks, source-system access, connector use, setup, or cross-domain switching
7. the area-specific docs for the task

### `Context check`

Report:

- repo name and path
- current branch and sync state
- worktree state, including ignored/private areas only when relevant
- active domain and likely workspace
- current handoff status
- default safety posture
- relevant docs to read next

### `Session health`

Run the context check plus any task-specific readiness checks below.

## Default Posture

ONL Brain is privacy-aware, decision-oriented, and continuity-focused.

Default to:

- narrow reads tied to the user's request
- summaries and links instead of copying raw sensitive source content
- drafts and recommendations unless the user explicitly requests a permitted write
- no Gmail or Google Calendar browsing without a bounded reason
- no calendar writes
- no external source-system writes unless explicitly allowed by [Access and Safety](access-and-safety.md)

## Local Checks

Useful baseline commands:

```bash
git status --short --ignored --branch
git log --oneline -5
test -f .env && echo ".env present" || echo ".env missing"
python3 --version
```

Interpretation:

- `.env` is needed for Todoist, analytics, and future API-backed work. Check presence only; do not print values.
- Python is needed for the current local analytics and Todoist toolkits.
- A dirty worktree may represent active ministry notes or generated outputs. Preserve existing work before editing.

## Connector Checks

Only check a connector when the task actually needs it.

### Google Drive and Docs

Use when planning docs, source documents, or external docs are explicitly involved.

- keep reads bounded to the named file, folder, or topic
- summarize durable implications into the repo instead of copying whole private documents
- do not edit Drive files unless the user explicitly requests that document edit

### Gmail

Use only for narrow, user-requested searches or reads.

- do not browse broadly for context
- do not send email except an explicitly requested self-email to `bfiles@northridgerochester.com`
- avoid copying raw pastoral, staff, or private email content into the repo

### Google Calendar

Use only for bounded planning or availability questions.

- read-only
- no create, update, delete, RSVP, invite, or scheduling actions
- summarize schedule implications without unnecessary event detail

### Todoist

Treat Todoist as read-only unless Brad explicitly requests a specific write.

Check `tools/todoist/README.md` before using the local toolkit.

### RockAgent

Use RockAgent only when ONL work needs Rock evidence, Rock configuration, Rock Workbench artifacts, or Rock source/manual context.

Do not make RockAgent a required health check for ordinary ONL documentation or planning work.

### Atlassian

Use Atlassian only when the ONL work is actually tracked in Jira or Confluence, or when promoting stable ONL knowledge to Confluence.

### Chrome DevTools

Use browser automation only when a task requires inspecting or interacting with a web UI. Treat production-control pages as high impact and ask before saving changes.

## Workflow Checks

### Online Analytics

Before analytics reporting work:

- read [Online Analytics Reporting](../operations/analytics-reporting.md)
- read [Online Analytics Metrics](../dashboards/online-analytics-metrics.md)
- read [Online Analytics Toolkit](../../tools/analytics/README.md)
- verify `.env` presence if API-backed source collection is needed
- keep raw exports or sensitive account details out of the repo unless intentionally sanitized

### Source Digestion

Before digesting external docs, emails, exports, or reports:

- identify the source system
- confirm whether the source is canonical, archival, a work queue, or a tooling system
- preserve the distinction between raw source material and durable repo knowledge
- store summaries in the appropriate `docs/` area, not in the repo root

### Private Workspaces

Confidential 360-review material belongs under `docs/workspaces/360-reviews/private/`, which is git-ignored.

Before discussing, summarizing, or moving private workspace material, verify that the user asked for that specific workspace.

## Dashboard Summary

Use this compact shape after a context or health check:

```text
Context Check
- Repo:
- Path:
- Branch:
- Worktree:
- Sync:
- Domain:
- Active workspace:
- Handoff:
- Default posture:

Session Health
- Local tools:
- .env:
- Connectors needed:
- Source-system boundaries:
- Private workspace risk:
- Recommended action:
```

## Cross-Domain Notes

ONL Brain should link to adjacent repos and summarize durable ministry implications, not absorb their artifacts.

- ScriptBrain owns the host script corpus, writing workflow, and script-analysis tooling.
- Rock Workbench owns Rock RMS operational SQL, Lava, HTML, and reporting artifacts.
- rock-agent owns the local MCP service and Rock access layer.

When switching domains, run the target repo's `Context check` before editing there.
