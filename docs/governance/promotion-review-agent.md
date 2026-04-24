# Promotion Review Agent

This document describes a recurring review role for deciding what content in the repo should be promoted to Confluence.

It may eventually be performed by an actual agent, but it can also be done manually as a lightweight editorial review.

## Purpose

Protect the distinction between:

- repo as the source of operational truth
- Confluence as the team-friendly presentation layer

## Mission

Review the repository periodically and identify content that is mature enough, useful enough, and audience-ready enough to become a Confluence page or Confluence update.

## What the reviewer looks for

- Documents that have become stable and are no longer rough notes
- Repo pages that would help staff or serve team members if rewritten for easier reading
- Operational changes that affect how the team works
- Repeatedly referenced docs that deserve a simpler front door in Confluence
- Areas where Confluence is now stale compared to the repo

## Promotion criteria

Content is a good candidate for Confluence when it is:

- Stable enough that frequent line-level revision is unlikely
- Useful to a broader audience than repo contributors
- Important for onboarding, coordination, or team clarity
- Better presented as a readable guide than as a system definition

## Do not promote when

- The content is still exploratory
- The content is deeply technical or highly structured
- The content is mainly a template or source artifact
- The content changes too often to maintain in two places responsibly

## Review cadence

Recommended:

- Quick scan weekly during active build-out
- Formal review monthly
- Broader audit quarterly

## Review checklist

- Which repo docs changed materially since the last review?
- Which of those changes affect staff, serve team members, or leadership visibility?
- Which docs are now stable enough to publish outward?
- Which Confluence pages are stale or missing?
- Which pages need a summary version instead of direct duplication?

## Suggested outputs

After each review, produce:

- A short list of docs to promote
- A short list of docs to update in Confluence
- A short list of docs that should remain repo-only
- Any drift or ownership risks discovered

## Example recommendation format

- Promote `docs/operations/weekly-checklist.md` into a staff-facing "Online Weekend Runbook" page.
- Adapt `docs/roles/serve-team-roles.md` into a serve team recruitment overview.
- Keep `data/weekly-scorecard.csv` repo-only.
- Update Confluence onboarding because role expectations changed.

## Ownership options

This review role could be owned by:

- the online campus pastor
- an operations lead
- a ministry communications partner
- a future agent tasked with repo-to-Confluence promotion review

## If implemented as an agent

The agent should:

- read changed files in the repo
- classify each document as repo-only, promote, or update-linked-page
- explain why
- suggest the likely Confluence audience
- avoid recommending duplication of structured source artifacts

## Success measure

The system is healthy when:

- the repo remains the precise operational backbone
- Confluence stays readable and current
- the team can trust both without guessing which one matters more
