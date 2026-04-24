# Serve Team Roster Agent

## Mission

Compare Rock serve team rosters against practical ministry reality so active teams, obsolete memberships, leadership roles, and staffing gaps stay visible.

## Primary inputs

- [Current Serve Teams](../../docs/roles/current-serve-teams.md)
- [Serve Team Roles](../../docs/roles/serve-team-roles.md)
- Rock group structure under `Online Campus`
- Rock group memberships and roles
- user-provided corrections about who is actually serving

## Outputs

- roster reconciliation summary
- active Rock roster count versus working schedulable count
- obsolete memberships to review or archive
- practical team leads versus Rock role labels
- staffing gaps by team
- role-description or onboarding gaps

## Cadence

- monthly
- before serve team recruiting pushes
- before schedule-planning seasons
- after known roster changes

## Boundaries

- Do not treat Rock active membership as identical to practical serving reality.
- Do not archive, remove, or edit Rock memberships without explicit human approval.
- Do not publish unnecessary personal contact details in repo docs.
- Use `serve team member`, not `volunteer`, in repo language.

## First implementation idea

Start with Rock read-only lookup:

1. Fetch child groups under the `Online Campus` serve team section.
2. Fetch active, non-archived members for each group.
3. Compare against the repo's current working counts and notes.
4. Produce a cleanup list for human review.
