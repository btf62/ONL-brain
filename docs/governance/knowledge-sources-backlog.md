# Knowledge Sources Backlog

This document captures possible source systems and archives that may contain useful knowledge for the online campus operating system.

The goal is not to ingest everything immediately. The goal is to remember where important knowledge may live, decide what kind of digest would be useful, and route durable operating knowledge into the right part of the repo.

For source-system vocabulary and categories, see [Source Systems](source-systems.md).

## Source systems to consider

### Google Drive: Northridge files

Likely value:

- years of online service scripts
- scattered ministry documentation
- giveaway process documents
- shared-drive playbooks or job descriptions
- historical examples of recurring online campus work

Current thought:

- script archives may be handled by a separate Script Brain archive or repo
- this repo should probably know that Script Brain exists, but should not duplicate every script
- stable processes discovered in Drive can become repo docs or templates

Possible repo outputs:

- operations checklist updates
- giveaway workflow documentation
- role descriptions for recurring writing or admin tasks
- links or summaries of official job descriptions and playbooks

### Script Brain archive or repo

Likely value:

- long-term script memory
- writing patterns
- examples of weekly online-specific language
- future agents that help draft new scripts

Current thought:

- this is probably a separate system
- weekly scriptwriting is still a major online campus responsibility
- scriptwriting may be unlikely to delegate, but it should still be named as a defined responsibility

Possible repo outputs:

- script writer role description
- weekly scriptwriting checklist
- boundary note explaining how this repo relates to Script Brain
- source link from operations docs to the external script archive

Related repo:

- [Related Repositories](related-repositories.md)

### Adjacent local repositories

Likely value:

- tool access to Rock RMS through Rock Agent
- script corpus and scriptwriting support through ScriptBrain
- Rock sysadmin and development artifacts through Rock Workbench

Current thought:

- these should remain separate repositories
- this repo should be aware of them because they support recurring online campus work
- durable online campus process knowledge can be summarized here when those repos reveal it

Possible repo outputs:

- related-repositories index
- role or workflow docs that link to the adjacent repo responsible for implementation
- boundary notes that prevent duplicate documentation

Related doc:

- [Related Repositories](related-repositories.md)

### Gmail or email digests

Likely value:

- undocumented giveaway logistics
- recurring admin handoffs
- prior communication patterns
- clues about who owned what historically
- examples of past online campus processes

Current thought:

- direct email ingestion should be cautious because email contains private, sensitive, and noisy material
- a separate tool, such as Gemini, could create targeted digests for review before anything enters this repo
- only durable process knowledge should be copied into the repo
- Gmail access must follow the narrow-search, narrow-read, never-send rules in [Source Systems](source-systems.md)

Possible repo outputs:

- giveaway workflow summary
- admin support role description
- recurring communication templates
- list of source emails or date ranges reviewed, without private email content

### Google Calendar

Likely value:

- recurring staff and online campus rhythms
- staff travel constraints
- weekly and seasonal planning context
- evidence for dashboard cadence and operating-rhythm design

Current thought:

- calendar access should be read-only and only used for specific user-requested questions
- the two likely relevant calendars are `Staff Travel/Vacation Schedule` and Brad's primary work calendar, `bfiles@northridgerochester.com`
- calendar data may inform cadence docs, but should not become canonical process documentation by itself
- Google Calendar access must follow the narrow-read, no-scheduling, no-modification rules in [Source Systems](source-systems.md)

Possible repo outputs:

- operating rhythm summary
- dashboard cadence notes
- recurring meeting or planning-pattern inventory
- list of date ranges reviewed, without unnecessary event details

### Shared drives and team documentation

Likely value:

- official Northridge job description
- online campus playbook
- staff-facing playbooks
- shared process documents
- historical docs that clarify expectations

Current thought:

- official documents should be preserved as source artifacts or summarized with links
- if a document is currently canonical elsewhere, this repo should reference it instead of silently replacing it

Possible repo outputs:

- archive summary for official source docs
- updated online campus pastor job description
- playbook gap list
- Confluence promotion candidates

Related doc:

- [Source Documents](source-documents.md)

### Rock key leader and community group dashboards

Likely value:

- assigned key leaders Brad is responsible to contact throughout the year
- touchpoint history for texts, calls, emails, visits, hallway conversations, coffee, meals, and other leader-care interactions
- assigned community groups and community group leaders Brad coaches
- evidence for leadership-care dashboards and weekly closed-list planning

Current thought:

- Rock should remain canonical for assignments and logged touchpoints
- this repo should define the responsibility, dashboard questions, and coaching rhythm
- live Rock review should be narrow and tied to a specific question or dashboard build-out

Possible repo outputs:

- leadership-care responsibility doc
- key leader dashboard questions
- community group coach dashboard questions
- weekly or monthly leadership-care review checklist
- small groups coach playbook summary if one exists

Related doc:

- [Leadership Care Responsibilities](../people/leadership-care-responsibilities.md)

### Giveaway documentation

Likely value:

- recurring process that happens three or four times per year
- admin-support task that used to be delegated
- concrete workflow with likely checklists, deadlines, communications, and fulfillment steps

Current thought:

- this is a strong candidate for documentation because it is recurring, operational, and delegable
- the workflow probably belongs in `docs/operations/`
- the human support role probably belongs in `docs/roles/`

Possible repo outputs:

- online giveaway workflow
- giveaway checklist
- admin support role description
- giveaway communication templates

## Ingestion principles

- Start with summaries before importing large source collections.
- Preserve original source artifacts only when they explain important context or would be hard to recover later.
- Keep private, sensitive, or person-specific email content out of the repo unless there is a clear reason and it has been reviewed.
- Prefer linking to external canonical systems when those systems should remain the source of truth.
- Convert recurring work into checklists, role descriptions, templates, or dashboard metrics.
- Treat rough digests as source material, not final operating truth.

## Triage questions

For any source or digest, ask:

- What recurring work does this explain?
- Who currently owns the work?
- Could this be delegated to staff, a serve team member, an admin, or an agent?
- Does this belong in operations, roles, people, dashboards, archive, or governance?
- Is the source canonical elsewhere, or should this repo become canonical?
- What sensitive information should be omitted?

## Current high-value next digests

1. Giveaway process digest from Google Drive and email history.
2. Official online campus pastor job description or playbook digest.
3. Scriptwriting responsibility summary, including what belongs in this repo versus Script Brain.
4. Shared-drive scan for online campus process documents.

## Open questions

- Where should the repo link to the Script Brain archive or repo?
- Does Northridge already have a canonical playbook location, or should this repo become the structured source?
- Which giveaway tasks are appropriate for an admin to own end to end?
- Which Google Drive folders are most likely to contain current, not merely historical, operating knowledge?
