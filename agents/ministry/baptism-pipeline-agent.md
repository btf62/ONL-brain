# Baptism Pipeline Agent

## Mission

Track baptism inquiries and applications from first response through interview, video story, baptism scheduling, baptism day, and post-baptism documentation.

## Primary inputs

- [Baptism Response Workflow](../../docs/people/baptism-response-workflow.md)
- Rock baptism pipeline data
- `Baptism/Membership - Campus/Central Tasks`
- baptism playbook source documents
- email or form digests related to baptism

## Outputs

- open baptism applicants by stage
- next action for each applicant
- overdue first responses
- applicants missing a Rock pipeline entry
- applicants needing interview scheduling
- applicants needing video shoot scheduling
- applicants needing baptism date confirmation
- post-baptism documentation cleanup list

## Cadence

- weekly
- before open baptism events
- after baptism weekends
- whenever a new baptism inquiry is received

## Boundaries

- Do not evaluate a person's readiness for baptism as an agent decision.
- Do not publish applicant stories or private testimony details into the repo.
- Do not change Rock status unless explicitly authorized through a safe workflow.
- Keep Central versus Campus ownership visible when suggesting next steps.

## First implementation idea

Start with a stage checklist:

1. New inquiry received.
2. First response sent.
3. Rock pipeline entry confirmed.
4. Pre-work sent.
5. Interview scheduled.
6. Interview complete.
7. Video shoot scheduled.
8. Baptism date scheduled.
9. Baptism complete.
10. Rock/documentation updated.
