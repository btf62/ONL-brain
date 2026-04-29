# Church Online Chat Transcript Archive

## Proposal

Create a recurring weekly workflow that downloads Church Online Platform chat transcript zip files and stores any missing files in the local archive.

Church Online Platform generates transcript bundles for online services. Each bundle may include:

- host chat
- general/public chat
- one-on-one chats

These transcripts are useful as source artifacts for pastoral awareness, response review, historical context, and possible future source digestion. They should not be copied into this repo because they can include private conversations, prayer-adjacent content, and personally identifying details.

## Current Local Archive

Canonical local archive path:

```text
/Users/bradfiles/Documents/chop/archive
```

Observed local state on April 29, 2026:

- 421 transcript zip files
- earliest observed file: `2022-03-27T0900-0400 - Final Words - Part 5 - Transcripts.zip`
- latest observed file: `2026-04-12T0900-0400 - Deliverer - Part 1 - Transcripts.zip`

The archive folder appears case-insensitively as `chop`, `ChOP`, or `CHOP` on macOS. Use the lowercase path above in documentation and scripts.

## Current Manual Workflow

Current cadence:

- Periodically open Church Online Platform admin.
- Locate generated chat transcript bundles for recent services.
- Download transcript zip files.
- Save them to `/Users/bradfiles/Documents/chop/archive`.
- Avoid redownloading files that already exist locally.
- Catch up on any missing weeks when the archive falls behind.

## First-Pass Requirements

### Inputs

- Church Online Platform service/event list.
- Available transcript zip files for each service.
- Local archive inventory from `/Users/bradfiles/Documents/chop/archive`.
- A date range to check. Default should be recent weeks, with an option for a broader catch-up pass.

### Output

- Missing transcript zip files downloaded into the local archive.
- A short run summary showing:
  - date range checked
  - files already present
  - files downloaded
  - services with no transcript available
  - errors or authentication issues

### Matching Rules

The current archive filenames include:

```text
YYYY-MM-DDTHHMM-ZZZZ - Service Title - Transcripts.zip
```

The automation should compare candidate downloads against local filenames before downloading.

At minimum, match on:

- service start date and time
- service title when available
- transcript zip suffix

If Church Online Platform exposes stable service or event IDs, the automation should store or derive a manifest later so filename changes do not create duplicate downloads.

### Timing

Target cadence:

- weekly after transcripts are generated for the prior weekend

Recommended default:

- check the previous 2 to 4 weeks every run

Catch-up mode:

- accept a wider date range and download anything missing

## Safety And Privacy

- Do not commit transcript zip files to this repo.
- Do not copy raw transcript content into repo docs.
- Treat one-on-one chats and prayer-adjacent conversations as sensitive.
- Use transcript contents only for a clearly bounded purpose, such as response follow-up, source digestion, or incident review.
- If summaries are created later, avoid unnecessary names, chat text, or private details.
- Any automation should download only transcript files and should not modify Church Online Platform events, services, attenders, chats, or settings.

## Automation Sketch

### Phase 1: Inventory Checker

Create a local read-only inventory command that lists existing archive files and reports coverage by date.

Possible output:

- total zip count
- earliest and latest archived service
- recent Sundays with no matching transcript
- duplicate-looking files

This can be implemented without Church Online Platform access.

### Phase 2: Manual-Download Assistant

If direct platform access is not available yet, create a checklist-assisted flow:

1. Run the local archive inventory.
2. Identify recent missing service dates.
3. Manually download missing transcript zip files from Church Online Platform.
4. Save them to `/Users/bradfiles/Documents/chop/archive`.
5. Re-run the inventory and confirm the gap is closed.

### Phase 3: Platform Download Automation

If Church Online Platform exposes a supported API, authenticated export route, or reliable admin download endpoint:

1. Authenticate with least-privilege access.
2. Fetch services/events for the configured date range.
3. Fetch available transcript bundle metadata.
4. Compare against local archive filenames or a manifest.
5. Download only missing zip files.
6. Write a run summary.

### Phase 4: Scheduled Check

Once the download process is reliable:

- schedule a weekly local run
- default to dry-run/report mode first
- notify Brad or write a local log if downloads fail
- avoid unattended changes outside the transcript archive folder

## Open Questions

- Does Church Online Platform expose transcript bundles through a supported API?
- If not, is browser automation against the admin UI acceptable?
- What login/session mechanism should a local script use safely?
- How long after a service are transcript zip files reliably available?
- Do all services generate transcripts, including special services and holiday services?
- Should the local archive have a manifest file outside the repo, or is filename-based detection enough?
- Should transcript coverage be checked against ScriptBrain service dates, Church Online Platform events, or the local archive only?
- Should transcript summaries ever be created, and if so where should sensitive summaries live?

## Related Docs

- [Weekly Checklist](weekly-checklist.md)
- [Source Systems](../governance/source-systems.md)
- [Access and Safety](../governance/access-and-safety.md)
- [Source Digest Agent](../../agents/ministry/source-digest-agent.md)
