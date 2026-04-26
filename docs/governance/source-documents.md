# Source Documents

This document tracks external source documents that may shape this repo.

The repo should summarize durable operating knowledge from these sources without silently replacing the external document if that document remains canonical elsewhere.

For the broader map of tools, databases, repositories, and queues, see [Source Systems](source-systems.md).

## Google Drive documents found

### Campus Pastor Responsibilities (2024)

Drive title:

- `Campus Pastor Responsibilities (2024)`

URL:

- `https://docs.google.com/document/d/1xeGjiLTL_Lnm-kCRMswLOf_xhajBA27rlzHM-ypt8R4`

Why it matters:

- describes the online campus pastor role around vision, operations, and people
- names weekly responsibilities such as Sunday service readiness, connections follow-up, media production, and website management
- includes older but valuable details about talking points, CHOP setup, PCO, ProPresenter, Subsplash, and connections follow-up
- names historic online roles, including admin volunteer, tech lead, chat host lead, co-hosts, and production roles

Likely repo outputs:

- refine [Online Campus Pastor Job Description](../roles/online-campus-pastor.md)
- expand [Production Workflow](../operations/production-workflow.md)
- expand [Connection Pipelines](../people/connection-pipelines.md)
- create a fuller online campus playbook

### Brad Files - Job Description

Drive title:

- `Brad Files - Job Description`

URL:

- `https://docs.google.com/document/d/10eCdxBZxjOMpZdjMN2hloc8tIogpBofAlzu1KQhAz6A`

Why it matters:

- blends Rock project coordination and online campus pastor assistant responsibilities
- includes Rock database training, project development, troubleshooting, and staff support
- includes online campus leadership, weekend process ownership, assimilation, next steps, metrics reporting, and pastoral care

Likely repo outputs:

- clarify the boundary between online campus pastor work and Rock sysadmin/development work
- connect this repo to [Related Repositories](related-repositories.md)
- update role descriptions and role map as current expectations become clearer

### Central/Campus Playbook: Connections

Drive title:

- `Central/Campus Playbook: Connections - Complete`

URL:

- `https://docs.google.com/document/d/1gR9eOUHg__vWIp2fznP-X9SH1tmFG-hr1_txFCwuT14`

Why it matters:

- defines Connections around helping everyone take next steps at Northridge
- includes the standard that contact is initiated within 24 hours of a request for information
- describes three contact attempts over three weeks for specific next-step inquiries
- names `iwant.info` as a central next-step source
- distinguishes central and campus responsibilities for follow-up

Likely repo outputs:

- anchor online community response targets
- refine first-response expectations for prayer, baptism, membership, serving, and group interest
- add dashboard metrics for overdue follow-up

### Central/Campus Playbooks

Drive sources found:

- `Central/Campus Playbook: Baptism - Complete`
- `Central/Campus Playbook: Membership - Complete`
- `Central/Campus Playbook: Production - Complete`
- `Playbooks List`

Why they matter:

- provide central/campus standards for major ministry pathways
- clarify which responsibilities are central and which belong to the campus
- may be the best source for official expectations before this repo adapts online-specific workflows

Likely repo outputs:

- archive summaries for each playbook that materially affects online campus operations
- online-specific adaptations where the central/campus playbook does not directly cover online realities
- Confluence promotion candidates once repo docs stabilize

### Baptism/Membership - Campus/Central Tasks

Drive titles:

- `Baptism_Membership - Campus_Central Tasks.xlsx`
- `Baptism/Membership - Campus/Central Tasks`

URLs:

- `https://drive.google.com/file/d/1VzET_NfEiUOIPWQKexlpkffM5oIWXGtF`
- `https://docs.google.com/spreadsheets/d/1noPet-juRh2n17T-WpauyH7AF2S5xBlVf-j1pIL5Te4`

Why it matters:

- gives the task-level handoff between Campus and Central for baptism and membership
- identifies Campus ownership of initial contact, interview, video scheduling, baptism date scheduling, practice/preparation, and baptism day
- identifies Central ownership of Rock pipeline updates, application organization, supplies, documentation, and weekly update notifications
- includes CP notes suggesting the initial communication and Rock pipeline ownership may need clarification

Likely repo outputs:

- [Baptism Response Workflow](../people/baptism-response-workflow.md)
- refined Rock pipeline/status documentation
- clarified online-campus first-response ownership

## Public vendor references checked

### Church Online Platform Analytics

URL:

- `https://support.online.church/l/en/article/abqorbtzx6-overview-analytics`

Why it matters:

- defines Church Online Platform admin analytics such as attendance, unique viewers, peak concurrent attenders, chat participation, prayer sessions, and Moment engagement
- clarifies that Church Online Platform analytics are platform-attender metrics rather than general streaming-provider views

Likely repo outputs:

- [Online Analytics Reporting](../operations/analytics-reporting.md)
- [Online Analytics Metrics](../dashboards/online-analytics-metrics.md)

### Resi Analytics and Go Live API

URLs:

- `https://resi.io/features/analytics/`
- `https://resi.io/go-live-api/`

Why it matters:

- documents Resi's analytics, exports, live/on-demand reporting, social analytics, and destination-level stream context
- confirms a public Go Live API exists for production control, while analytics automation still needs verification

Likely repo outputs:

- Resi source-system boundary
- analytics export workflow
- future API investigation task

### YouTube Analytics API

URLs:

- `https://developers.google.com/youtube/analytics/`
- `https://developers.google.com/youtube/analytics/reference/reports/query`
- `https://developers.google.com/youtube/analytics/metrics`

Why it matters:

- confirms YouTube has an official Analytics API for targeted reports
- identifies read-only reporting scopes and metrics such as views, watch time, average view duration, and livestream concurrent viewer metrics

Likely repo outputs:

- future YouTube read-only connector in `tools/analytics/`
- normalized YouTube fields in [Online Analytics Metrics](../dashboards/online-analytics-metrics.md)

## Confluence spaces found

### Northridge ONL Operations

URL:

- `https://northridgerochester.atlassian.net/wiki/spaces/NOO/overview`

Atlassian metadata:

- Cloud ID: `e8e778fe-0681-412e-b4b9-0519a052c9ed`
- Space key: `NOO`
- Space ID: `111706116`
- Overview page ID: `111706430`

Why it matters:

- this is the companion Confluence space for team-facing online campus documentation
- the overview page describes it as the documentation wiki for Northridge ONL vision, operations, and pastoring
- it should become the presentation and discovery layer for stable repo content

Likely repo outputs:

- keep [Repo and Confluence Boundary](repo-confluence-boundary.md) current
- promote stable online campus playbook material into this Confluence space
- use Confluence for readable team-facing summaries while preserving structured operational truth in this repo

## Open source-document questions

- Which Drive folder should be treated as the canonical home for current Northridge playbooks?
- Does an official online campus-specific playbook already exist, or should this repo become the structured draft?
- Which job description is current for the online campus pastor role versus older assistant or hybrid role definitions?
- Which source documents should be archived locally, and which should only be linked and summarized?
