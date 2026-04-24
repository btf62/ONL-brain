# Repo and Confluence Boundary

This document defines the healthy division of labor between this repository and Confluence.

## Purpose

The repo and Confluence should support one another, not compete with one another.

The repo is the system of record for structured ministry operations.
Confluence is the communication and discovery layer for the team.

## Core principle

- Put systems in the repo.
- Put communication in Confluence.

## Repo is canonical for

- Role definitions and job descriptions
- Repeatable checklists and workflows
- Structured operating procedures
- Pipeline definitions and status logic
- Metrics definitions and dashboard schemas
- Templates and reusable artifacts
- Data files that may later support reporting or automation

## Confluence is canonical for

- Team-facing overview pages
- Serve team onboarding hubs
- Readable ministry playbooks
- FAQ-style knowledge pages
- Meeting notes and working discussions
- Cross-team communication pages
- Curated summaries of repo content for broad audiences

## Translation rule

The repo should usually contain the precise source material.
Confluence should usually contain the adapted, readable, audience-specific presentation of that material.

## Decision test

Put content in the repo when it:

- Needs version control
- Has a structured format
- Will be reused as a template
- May feed dashboards, reports, or automation
- Defines official process or operational logic

Put content in Confluence when it:

- Needs to be easily browsed by staff or serve team members
- Benefits from a wiki-style reading experience
- Exists mainly to orient, explain, or socialize information
- Will be referenced in meetings, onboarding, or team communication

## Source-of-truth rule

Every content type should have one canonical home.

Examples:

- Weekly checklist template: repo canonical
- Serve team onboarding portal: Confluence canonical
- Rock RMS pipeline field definitions: repo canonical
- Staff guide for handling baptism follow-up: Confluence canonical, based on repo workflows
- Dashboard metric definitions: repo canonical
- Leadership summary page with narrative commentary: Confluence canonical

## Recommended workflow

1. Draft and refine operational truth in the repo.
2. Promote stable, useful material into Confluence.
3. Adapt the writing for the target audience instead of copying blindly.
4. Link repo and Confluence pages so the relationship stays visible.
5. Review regularly for drift.

## Anti-patterns to avoid

- Keeping the same procedure fully maintained in both places
- Using Confluence as the only home for structured operational logic
- Using the repo as the only place serve team members must go for basic orientation
- Publishing unfinished internal notes to Confluence without clarification

## Maintenance expectation

If the repo changes in a way that affects team understanding, the corresponding Confluence page should be reviewed for promotion or update.
