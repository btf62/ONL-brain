# Thursday Online Service Prep Rhythm

## Proposal

Reserve Thursdays from 10:00 AM to noon for online service preparation.

This block has two mostly independent lanes:

- ScriptBrain writing room for the online co-hosting script.
- Order-of-service and studio preparation for Sunday's online service.

The lanes can happen in the same protected time block, but they should not be treated as one tightly coupled workflow. The writing room can usually proceed on its own. The order-of-service and studio-prep lane depends on the video production team finishing the edited videos and posting them online.

## Cadence

Default weekly rhythm:

- Thursday, 10:00 AM to noon

Primary purpose:

- protect a predictable weekly block for scriptwriting and online-service readiness

## Lane 1: ScriptBrain Writing Room

Purpose:

- write or revise the online co-hosting script for the upcoming Sunday
- use ScriptBrain as the writing-room support system
- turn service notes, message context, co-host needs, and online-specific moments into a usable script

Inputs:

- upcoming service date
- message or sermon focus
- known online-specific announcements or calls to action
- co-host information if available
- ScriptBrain writing-room workflow and corpus context

Output:

- draft or final online co-hosting script for Sunday
- any follow-up questions or missing source context

Boundary:

- ScriptBrain owns the script corpus, script retrieval, style patterns, and writing-room tooling.
- ONL Brain owns the weekly operating rhythm and the fact that this block should happen.

## Lane 2: Orders Of Service And Studio Prep

Purpose:

- make sure Sunday's service materials are ready in print and in the studio
- update ProPresenter with Sunday's content

Tasks:

1. Print current orders of service.
2. Review and update the orders of service.
3. Print the finalized orders of service.
4. Take the finalized orders of service to the studio.
5. Update ProPresenter with Sunday's contents.

Prerequisite:

- video production team has finished editing the videos and posted them online

If the prerequisite is not met:

- keep the ScriptBrain writing room if possible
- review what can be prepared without final video assets
- mark the studio/ProPresenter update as waiting on video readiness
- avoid treating the whole Thursday block as failed just because the production-prep lane is blocked

Outputs:

- printed final orders of service
- studio copy delivered
- ProPresenter updated for Sunday's contents
- any missing media or production blockers named clearly

## Automation Sketch

### Phase 1: Checklist Prompt

User prompt:

```text
Run the Thursday online service prep rhythm.
```

Agent flow:

1. Confirm the upcoming Sunday date.
2. Start the ScriptBrain writing-room workflow or link to the needed ScriptBrain context.
3. Ask whether video production has finished editing and posted the videos online.
4. If yes, walk through order-of-service review, print, studio delivery, and ProPresenter update.
5. If no, preserve the production-prep tasks as blocked and continue with the writing-room lane.

### Phase 2: Task-System Support

Create or maintain a recurring task/reminder for Thursday 10:00 AM to noon.

Suggested task title:

```text
Thursday online service prep rhythm
```

Suggested checklist:

- ScriptBrain writing room for online co-hosting script
- Print current orders of service
- Review and update orders of service
- Print finalized orders of service
- Take finalized orders of service to studio
- Update ProPresenter with Sunday's contents

### Phase 3: Readiness Check

If video readiness becomes observable through a source system later, automation can check whether videos are posted online before prompting for the production-prep lane.

Until then, video readiness should be treated as a human-confirmed prerequisite.

## Open Questions

- Where is the canonical order-of-service source?
- What exact format should be printed for the studio copy?
- Where are final edited videos posted, and can that readiness be checked automatically?
- Is ProPresenter update manual-only, or is there a file/import workflow that can be documented?
- Should the Thursday block create Todoist subtasks, calendar time blocking, or both?
- Does the ScriptBrain writing-room flow need a specific prompt for co-hosting scripts?

## Related Docs

- [Weekly Checklist](weekly-checklist.md)
- [Production Workflow](production-workflow.md)
- [Related Repositories](../governance/related-repositories.md)
- [Source Systems](../governance/source-systems.md)
