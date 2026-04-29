# Agent Instructions

These are standing instructions for Codex or other AI agents working in this repo.

## Start here

Before doing work, read:

1. [README.md](README.md)
2. [HANDOFF.md](HANDOFF.md)
3. [Access and Safety](docs/governance/access-and-safety.md)
4. [Source Systems](docs/governance/source-systems.md)
5. [Session Health](docs/governance/session-health.md) when the task involves context checks, source-system access, connector use, setup, or cross-domain switching

Then read the task-specific docs linked from those files.

If the user says `Context check`, report the current repo, path, branch, sync state, worktree state, active domain/workspace, current handoff status, and default safety posture.

If the user says `Session health`, include the context check plus task-specific readiness checks from [Session Health](docs/governance/session-health.md).

When switching between ONL Brain, ScriptBrain, Rock Workbench, and rock-agent, run the target repo's context check before editing there.

## Working posture

- Treat this repo as the operating system for Brad's online campus pastor role.
- Preserve the distinction between durable operating knowledge, source artifacts, work queues, and private material.
- Prefer summarizing and linking source systems instead of copying raw sensitive content into the repo.
- Check `git status --short --ignored` before making or committing changes.
- Do not revert or overwrite user work unless Brad explicitly asks.
- Keep edits small, readable, and easy to review.

## Safety rules

- Follow [Access and Safety](docs/governance/access-and-safety.md).
- Gmail and Google Calendar access must be narrow and user-requested.
- Do not send email except an explicitly requested self-email to `bfiles@northridgerochester.com`.
- Do not create, update, delete, RSVP to, invite attendees to, or schedule Google Calendar events.
- Treat Todoist as read-only unless Brad explicitly requests a specific write.
- Do not commit `.env`, secrets, private HR/360 review content, or unnecessary sensitive pastoral/staff details.
- Keep confidential 360-review material in `docs/workspaces/360-reviews/private/`, which is git-ignored.

## Agent definitions

The repo's ministry and personal agent definitions live in [agents/](agents/).

- Use [agents/README.md](agents/README.md) to understand the current agent map.
- Personal agents support Brad's effectiveness and reflection.
- Ministry agents support ministry operations, dashboards, source digestion, and response workflows.
- Agents do not replace Brad's pastoral judgment, staff authority, or human relationship work.

## Source systems

Use [Source Systems](docs/governance/source-systems.md) as the map for external tools and databases.

Important current source systems include:

- Rock RMS and Rock Agent
- Google Drive
- Gmail
- Google Calendar
- Todoist
- Confluence
- ScriptBrain
- Rock Workbench

Access to a tool does not imply permission to browse it. Stay bounded by the user's explicit request.
