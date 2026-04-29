# ONL Brain

This repository is the operating system for the online campus pastor role.

It is organized around three primary areas of responsibility:

- Vision: Why the online campus exists, what it is trying to build, and how success is defined.
- Operations: The repeatable weekly work required to deliver a healthy online ministry experience.
- People: The shepherding, follow-up, care, and connection work required to pastor an online community well.

The long-term goal is to make this repository useful in four ways:

- Clarify responsibilities that are currently carried by one person wearing many hats.
- Document workflows well enough that serve team members and staff can step into defined roles.
- Create training and role descriptions that make recruiting easier.
- Build toward simple dashboards and checklists that show whether the ministry is healthy and on track.

## Repo structure

- `docs/vision/`: ministry purpose, outcomes, and measures of success
- `docs/operations/`: weekly production, technical systems, scripts, analytics, and checklists
- `docs/people/`: pastoral care, connection pathways, and follow-up systems
- `docs/roles/`: hats, job descriptions, role definitions, and serve team pathways
- `docs/dashboards/`: scorecards, KPIs, and dashboard planning
- `docs/archive/`: archived source material and interpretation notes
- `docs/governance/`: source-of-truth rules, publishing boundaries, and review workflows
- `agents/`: agent definitions and support systems, including personal and ministry agents
- `data/`: starter CSV files for scorecards and pipeline tracking
- `templates/`: reusable templates for new roles, workflows, and scorecards
- `tools/`: utility scripts and integrations that support ministry operations

## How to use this repo

For a new Codex session, start with [Agent Instructions](AGENTS.md) and [Session Handoff](HANDOFF.md). They name the restore prompt, safety boundaries, and first files to read.

Use `Context check` to report repo/path/branch/worktree/domain state.
Use `Session health` before source-system access, connector use, private workspace work, analytics reporting, or cross-domain switching. The local pattern lives in [Session Health](docs/governance/session-health.md).

Start with the overview docs:

1. Read [Vision Overview](docs/vision/README.md)
2. Read [Operations Overview](docs/operations/README.md)
3. Read [People Overview](docs/people/README.md)
4. Review [Role Map](docs/roles/role-map.md)
5. Run the ministry from [Weekly Checklist](docs/operations/weekly-checklist.md)

## Local setup

Use a local `.env` file for secrets and machine-specific configuration.

- Keep real values in `.env`
- Use `.env.example` as the shared template
- Never commit real tokens or credentials

Current environment variables we may use in local tools:

- `TODOIST_API_TOKEN`
- `OPENAI_API_KEY`
- `ATLASSIAN_CLOUD_ID`

## Suggested build order

If we keep developing this repo, a practical sequence is:

1. Finalize the purpose and success metrics of the online campus.
2. Document the recurring weekly ministry and production workflow.
3. Name each hat currently worn by the online campus pastor.
4. Convert hats into role descriptions with clear ownership.
5. Build serve team onboarding and training for the roles that can be delegated.
6. Add lightweight dashboards using the metrics framework in `docs/dashboards/`.

## Current assumptions

This first pass assumes:

- The online campus pastor currently owns many responsibilities across strategy, production, and pastoral care.
- Rock RMS is a key system for tracking people, next steps, and follow-up pipelines.
- The immediate need is documentation and structure, not a fully automated dashboard system yet.

Those assumptions can be refined as the repo grows.
