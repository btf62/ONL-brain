# Access and Safety

This document defines how agents and tools may interact with sensitive source systems.

The goal is useful assistance without accidental overreach.

## Core posture

- Access does not imply permission to browse.
- Read access should be narrow, purposeful, and tied to a user-requested question.
- Write-capable tools may exist, but agents must treat them as read-only unless a specific documented exception exists.
- Sensitive personal, pastoral, financial, and staff information should be summarized only when needed and should not be copied into the repo unnecessarily.
- Confidential HR review content should not be committed to the repo.
- Humans decide and act; agents prepare, summarize, flag, and recommend.

## Hard prohibitions

- Never send email to anyone other than Brad's own authenticated work account, except where a specific self-email exception below applies.
- Never create calendar events.
- Never update, move, delete, RSVP/respond to, invite attendees to, or otherwise modify calendar events.
- Never schedule on Brad's behalf.
- Never browse Gmail or Google Calendar broadly just to discover context.
- Never perform bulk reads or bulk imports from sensitive systems without a clearly bounded purpose and explicit permission.

## Gmail

Connected account:

- `bfiles@northridgerochester.com`

Allowed:

- narrow searches explicitly requested by the user
- narrow reads needed to answer the current question
- process summaries that avoid unnecessary private content
- draft copy when explicitly requested and left for human review
- sending a message to `bfiles@northridgerochester.com` only when Brad explicitly asks for an email to himself

Not allowed:

- broad exploratory searches
- bulk reading
- sending email to anyone other than `bfiles@northridgerochester.com`
- forwarding email
- archiving, labeling, deleting, or otherwise modifying messages unless explicitly approved for a specific action
- copying sensitive email or pastoral content into the repo unless there is a clear reason and human review

## Self-email exception

An agent may send email to `bfiles@northridgerochester.com` only when Brad explicitly requests a self-email.

Allowed uses:

- daily triage maps
- summaries Brad wants to keep in his inbox
- reminders or checklists Brad asks to send to himself

Rules:

- The only recipient may be `bfiles@northridgerochester.com`.
- Do not add CC or BCC recipients.
- Do not forward existing emails under this exception.
- Do not use this exception to contact another person indirectly.
- If the requested content includes sensitive details, summarize minimally and avoid unnecessary private content.

## Google Calendar

Primary calendars of interest:

- `Staff Travel/Vacation Schedule` (`qivhipcac206tap8okbbgojelo@group.calendar.google.com`)
- `bfiles@northridgerochester.com` primary calendar (`bfiles@northridgerochester.com`)

Allowed:

- narrow event searches explicitly requested by the user
- bounded availability or rhythm review for a specific planning question
- identifying recurring patterns when the date range and scope are clear
- summarizing schedule implications without unnecessary event detail

Not allowed:

- broad calendar browsing
- personal surveillance or activity summaries
- creating calendar events
- modifying calendar events
- RSVP/responding to invitations
- scheduling on Brad's behalf

## Agent architecture

Mail and calendar should not have autonomous manager agents at this stage.

Instead, Gmail and Google Calendar are source systems accessed through task-specific agents when needed.

Examples:

- The Online Response Queue Agent may request a narrow Gmail read for a specific response queue question.
- The Source Digest Agent may summarize a user-provided email digest or a narrow set of source messages.
- A future Operating Rhythm or Dashboard Agent may request a bounded calendar review for cadence design.

This keeps the architecture safer: agents own ministry outcomes, while source-system access remains governed, narrow, and auditable.

## Review habit

When adding a new connected source system, document:

- what account or system is connected
- what it is useful for
- what it must not be used for
- whether reads are allowed
- whether writes are forbidden or require explicit approval
- which agents, if any, may use it
