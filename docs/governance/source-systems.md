# Source Systems

This document defines the main systems, tools, databases, repositories, and work queues that feed the online campus operating system.

The umbrella term is `source system`.

Not every source system is canonical. Some are official databases, some are work queues, some are archives, and some are tools we use to inspect other systems.

Sensitive access boundaries are governed by [Access and Safety](access-and-safety.md).

## Source-system categories

### Canonical systems

Systems where the official current truth lives for a specific domain.

Examples:

- Rock RMS for people, groups, rosters, workflows, and ministry database records
- this repo for structured online campus operating knowledge
- official Drive or Confluence docs when leadership has designated them as current policy

### Source artifacts

Individual files that preserve important context.

Examples:

- PDFs
- spreadsheets
- Google Docs
- exported reports
- historical planning documents

Source artifacts may be archived, summarized, or linked, but they are not automatically canonical.

### Tooling systems

Tools that help inspect, query, transform, or automate source data.

Examples:

- Rock Agent
- Gemini-generated email digests
- ScriptBrain tooling
- local repo scripts

### Work queues

Systems where tasks, requests, or obligations arrive.

Examples:

- Gmail
- Google Calendar
- Todoist
- form notifications
- `TEXT HELLO`
- Rock workflows or connection requests

Work queues are important because people can fall through the cracks there, but they should not be treated as long-term documentation homes.

### Reference repositories

Sibling repos that own adjacent domains of work.

Examples:

- `rock-agent`
- `script-brain`
- `Rock-Workbench`

Reference repositories should remain separate, with this repo linking to them and summarizing only the durable online campus implications.

## Current source systems

### ONL-brain

Role:

- canonical structured operating system for online campus ministry knowledge

Use for:

- role definitions
- workflows
- checklists
- response standards
- source-system summaries
- dashboard definitions
- agent definitions

Do not use for:

- raw private email content
- full script corpus
- Rock implementation artifacts
- complete copies of external canonical documents unless intentionally archived

### Rock RMS

Role:

- canonical ministry database for people, groups, serve teams, workflows, rosters, attendance, and follow-up records

Use for:

- serve team roster lookup
- group and group type structure
- key leader dashboard evidence
- community group and group leader assignments
- connection and workflow status
- baptism and membership pipeline records
- ministry database evidence

Do not use for:

- prose playbooks
- repo documentation
- final pastoral judgment about what current ministry reality means

Note:

- Rock data may be stale and should be reconciled against practical ministry reality.

### Rock Agent

Role:

- tooling system and access layer for Rock RMS, Rock source references, manuals, and Rock Workbench files

Use for:

- read-only Rock lookups
- evidence gathering from Rock-related systems
- production Rock REST reads
- code/manual references when needed

Do not use for:

- storing ministry process
- replacing Rock RMS as the canonical database
- making live mutations without explicit approval and guardrails

### Google Drive

Role:

- source system for documents, sheets, scripts, playbooks, and archived source artifacts

Use for:

- official source documents
- shared-drive playbooks
- job descriptions
- source spreadsheets
- script archive material
- giveaway documentation

Do not use for:

- structured repo workflows once those workflows have been formalized here
- hidden duplicate copies of canonical repo docs

### Gmail

Role:

- work queue and historical source system
- connected work account: `bfiles@northridgerochester.com`

Use for:

- incoming requests
- giveaway logistics
- admin handoff history
- evidence for recurring workflows
- targeted digests created outside the repo

Access rules:

- Follow [Access and Safety](access-and-safety.md).
- Do not run broad Gmail searches unless the user specifically asks for one.
- Keep searches narrow by using a specific task, topic, sender, date range, label, or known workflow.
- Keep reads narrow; read only the messages needed to answer the current question or produce the requested digest.
- Do not bulk-read, archive, label, delete, forward, or otherwise modify emails without explicit approval.
- Drafting email copy may be allowed when explicitly requested, but drafts must remain reviewable by a human.
- Never send email through Gmail or any other email tool.

Do not use for:

- canonical process documentation
- long-term tracking of pastoral follow-up
- broad raw imports into the repo

### Google Calendar

Role:

- schedule source system and rhythm evidence

Primary calendars:

- `Staff Travel/Vacation Schedule` (`qivhipcac206tap8okbbgojelo@group.calendar.google.com`)
- `bfiles@northridgerochester.com` primary calendar (`bfiles@northridgerochester.com`)

Identification notes:

- `Staff Travel/Vacation Schedule` is the exact staff/travel calendar name exposed by Google Calendar.
- `bfiles@northridgerochester.com` is Brad's primary work calendar; targeted checks found the recurring `SRT` Monday 9:00-11:00 AM meeting and `Pre-Preach` Thursday 9:00-10:00 AM meeting there.

Use for:

- narrowly bounded schedule lookup when the user asks for it
- understanding staff/travel constraints for online campus planning
- identifying recurring ministry rhythms and cadence patterns
- checking availability only when explicitly requested

Access rules:

- Follow [Access and Safety](access-and-safety.md).
- Do not list, search, or read calendar events unless the user asks for a specific calendar question.
- Keep searches narrow by calendar, date range, event topic, person, or planning question.
- Read only the events needed to answer the current question.
- Do not browse calendars broadly to discover context.
- Do not create calendar events.
- Do not update, move, delete, RSVP/respond to, invite attendees to, or otherwise modify calendar events.
- Do not schedule on the user's behalf, even if a tool exposes that capability.

Do not use for:

- canonical process documentation
- personal surveillance or broad activity summaries
- replacing a dashboard, task manager, or operating rhythm doc
- making commitments about the user's time

### Todoist

Role:

- task and work-queue system

Use for:

- personal or operational task tracking
- reminders
- closed-list execution
- recurring follow-up prompts

Do not use for:

- canonical process definitions
- source-of-truth records for people or pastoral care

### Confluence: Northridge ONL Operations

Role:

- team-facing presentation and discovery layer

URL:

- `https://northridgerochester.atlassian.net/wiki/spaces/NOO/overview`

Use for:

- readable playbook pages
- staff and serve team orientation
- meeting notes
- project plans
- promoted summaries of stable repo content

Do not use for:

- structured source data that needs version control
- private pastoral details
- maintaining a full duplicate of repo procedures

### ScriptBrain

Role:

- reference repository and tooling system for online host script corpus and scriptwriting support

Use for:

- script archive extraction
- script style analysis
- future script retrieval and drafting support

Do not use for:

- online campus operating workflows outside the scriptwriting domain
- serve team rosters
- response queue tracking

### Rock Workbench

Role:

- reference repository for Rock RMS operational SQL, Lava, HTML, dashboard, and reporting artifacts

Use for:

- Rock admin/development artifacts
- reusable SQL and Lava
- reports and dashboard prototypes
- implementation details behind Rock-related online campus work

Do not use for:

- ministry playbooks
- online campus role definitions
- pastoral response standards

### Local files and archives

Role:

- source artifacts and local working material

Use for:

- preserving files worth archiving
- temporary analysis
- one-off source imports

Do not use for:

- hidden long-term documentation
- replacing the repo or official systems

## Decision rule

When a new system or artifact appears, ask:

- What kind of source system is this?
- Is it canonical for anything?
- Is it a work queue, source artifact, tooling system, or reference repo?
- What should this repo copy, summarize, link, or ignore?
- What sensitive information should stay out of the repo?

## Related documents

- [Knowledge Sources Backlog](knowledge-sources-backlog.md)
- [Source Documents](source-documents.md)
- [Related Repositories](related-repositories.md)
- [Repo and Confluence Boundary](repo-confluence-boundary.md)
