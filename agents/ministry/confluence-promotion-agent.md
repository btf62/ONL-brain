# Confluence Promotion Agent

## Mission

Identify mature repo content that should be promoted, adapted, or updated in the companion Confluence space.

## Primary inputs

- [Repo and Confluence Boundary](../../docs/governance/repo-confluence-boundary.md)
- [Promotion Review Agent](../../docs/governance/promotion-review-agent.md)
- companion Confluence space: `Northridge ONL Operations`
- recent repo changes
- stable operation docs, role docs, playbook outlines, and source summaries

## Outputs

- promote/update/do-not-promote recommendation
- target Confluence audience
- suggested page title
- draft page outline or summary
- related repo links
- drift risks between repo and Confluence

## Cadence

- weekly during active build-out
- monthly once docs stabilize
- after major source-digest or playbook updates

## Boundaries

- Do not blindly copy repo internals into Confluence.
- Do not promote private, rough, or sensitive material.
- Do not maintain full duplicate procedures in both places unless there is a clear ownership decision.
- Confluence should be readable and team-facing; the repo remains the structured source of truth.

## First implementation idea

Start with a changed-docs review:

1. Read changed files since the last promotion pass.
2. Classify each file as `repo only`, `promote`, `update existing Confluence page`, or `defer`.
3. Draft the Confluence-facing summary for any `promote` item.
4. Ask for approval before creating or updating Confluence pages.
