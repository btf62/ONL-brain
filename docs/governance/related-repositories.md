# Related Repositories

This document names nearby repositories that support the online campus pastor role but should remain separate systems.

The goal is repo awareness, not repo consolidation.

## Local sibling repositories

### Rock Agent

Local path:

- `/Users/bradfiles/Documents/Development/rock-agent`

Purpose:

- provides Codex and OpenAI workflows with access to Rock RMS source code, Rock Workbench files, Rock manuals, and production Rock RMS REST reads
- exposes the `rockAgent` MCP tools used by this repo for Rock lookup and evidence gathering

Relationship to this repo:

- this repo uses Rock Agent as a tool and evidence source
- Rock Agent source code and MCP implementation details should stay in the Rock Agent repo
- durable ministry process discovered through Rock Agent can be summarized in this repo

Use when:

- querying Rock group structure, rosters, campuses, LMS classes, communication lists, or other production Rock context
- checking Rock manuals or source behavior through the MCP server
- understanding how the Rock connector itself works

### ScriptBrain

Local path:

- `/Users/bradfiles/Documents/Development/script-brain`

Purpose:

- builds a human-readable knowledge base for Northridge online host scripts
- extracts script metadata and content from Google Drive
- supports future retrieval, style consistency, and script drafting

Relationship to this repo:

- this repo should know ScriptBrain exists because weekly scriptwriting is a major online campus responsibility
- the script corpus, extraction pipeline, and script-specific analysis should stay in ScriptBrain
- this repo may define the scriptwriting role, weekly checklist, and boundary between online campus operations and script tooling

Use when:

- analyzing years of host scripts
- improving script style consistency
- drafting or retrieving script examples

### Rock Workbench

Local path:

- `/Users/bradfiles/Documents/Development/Rock-Workbench`

GitHub repository name:

- `rock-workbench`

Purpose:

- stores operational SQL, Lava, HTML, and reporting artifacts for Rock RMS administration and analysis
- supports Rock sysadmin and development work
- keeps writable operational artifacts separate from official Rock source repos

Relationship to this repo:

- Rock Workbench is the home for Rock implementation artifacts
- this repo may reference Rock Workbench when online campus workflows depend on Rock reports, Lava, dashboards, or admin scripts
- ministry-facing process, role, and operations docs should live here when they are about online campus operations rather than Rock implementation

Use when:

- developing Rock SQL, Lava, HTML, dashboards, reports, or one-time support scripts
- preserving implementation artifacts for Rock admin/development work
- investigating Rock operational data outside the narrower ministry documentation layer

## Boundary rule

- Put online campus ministry operating truth in this repo.
- Put script corpus and script tooling in ScriptBrain.
- Put Rock connector tooling in Rock Agent.
- Put Rock implementation artifacts in Rock Workbench.

When a nearby repo produces insight that affects the online campus pastor role, summarize the durable conclusion here and link to the source repo or artifact when useful.
