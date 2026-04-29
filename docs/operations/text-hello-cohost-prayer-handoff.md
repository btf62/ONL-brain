# Text HELLO Co-Host Prayer Handoff

## Proposal

Create a recurring Tuesday workflow that prepares a co-host email with the names of people who texted `HELLO` during the previous Sunday's online service.

The ministry reason is simple: during service, the online host says something like, "Text HELLO to the announced number and we'll know you're here, and we'll be praying for you by name." Brad can already see those `TEXT HELLO` responses in Gmail, but the co-host should also receive the list so they can participate in praying by name.

The first version can remain human-reviewed. A later automation can gather the names, identify the previous Sunday's co-host from ScriptBrain context, draft the email, and leave it ready for review.

## Current Manual Workflow

Current cadence:

- Every Tuesday, review `TEXT HELLO` messages from the previous Sunday.
- In Gmail, use the `TEXT HELLO` label/folder.
- Filter mentally or visually to the messages that came in on the previous Sunday.
- Capture a screenshot of the visible message list, including names and dates.
- Send an email to that Sunday's co-host with a short thank-you and the screenshot.

Current email intent:

- Thank the person for co-hosting.
- Share the names of people who texted `HELLO`.
- Invite them to pray for those people by name.
- Reinforce that the co-host is part of the pastoral follow-up, not only the on-camera moment.

## First-Pass Requirements

### Inputs

- Previous Sunday date.
- Gmail messages under the `TEXT HELLO` label/folder for that Sunday.
- Sender/person names visible in the `TEXT HELLO` messages.
- Previous Sunday's co-host, likely available from ScriptBrain prompt or script context.
- Optional: prior sent Gmail examples from Brad to co-hosts about `TEXT HELLO`, used only as tone/template evidence.

### Output

A human-reviewable email draft for the previous Sunday's co-host.

The draft should include:

- a warm thank-you for co-hosting
- the previous Sunday date
- the list of names who texted `HELLO`
- a short line asking the co-host to pray for them by name
- a concise close

The automated version should not require a screenshot if the names can be extracted reliably from Gmail.

### Recipients

Primary recipient:

- the previous Sunday's online co-host

Open requirement:

- confirm where the co-host's email address should be sourced from if ScriptBrain only has the co-host name.

### Timing

Target day:

- Tuesday after the Sunday service

The workflow should use the previous Sunday, not the current date's calendar week in a vague way. For example, if run on Tuesday, April 28, 2026, the target service date is Sunday, April 26, 2026.

### Safety And Review

- Gmail reads must be narrow: `TEXT HELLO` label/folder plus the target Sunday date.
- Do not browse Gmail broadly to discover context.
- Do not send the email automatically under the current ONL Brain safety rules.
- Prepare the email as draft copy for Brad to review and send manually, unless a future approved workflow changes the send boundary.
- Do not copy raw private message content into the repo. The repo should document the workflow, not store weekly names.
- If prior sent Gmail examples are used for tone, read only the small set needed to model this specific recurring email.

## Automation Sketch

### Phase 1: Assisted Draft

User prompt:

```text
Prepare the Text HELLO co-host prayer handoff for last Sunday.
```

Agent flow:

1. Determine the previous Sunday date.
2. Find the co-host for that Sunday from ScriptBrain context.
3. Search Gmail narrowly for `TEXT HELLO` messages on that date.
4. Extract a deduplicated list of names.
5. Draft the email body for Brad to review.
6. Report any uncertainty, such as missing co-host email or ambiguous names.

### Phase 2: Repeatable Local Tool

Create a small local tool or documented agent command that accepts:

- `--service-date YYYY-MM-DD`
- optional `--cohost-name`
- optional `--cohost-email`

The tool should output:

- target date
- co-host
- extracted names
- draft subject
- draft body
- warnings or missing information

### Phase 3: Calendar Or Task Reminder

If useful later, add a Tuesday reminder in the task system. This should remind Brad to run the workflow, not send anything automatically.

## Draft Email Shape

Subject:

```text
Text HELLO names from Sunday
```

Body:

```text
Hey <Co-host>,

Thanks again for co-hosting this past Sunday. Here are the people who texted HELLO on <Sunday Date> after we invited them to let us know they were watching.

<Name list>

Thanks for praying for them by name this week. I am grateful for the way you help make the online service feel personal and pastoral.

Brad
```

## Open Questions

- What is the exact Gmail label name as exposed through the Gmail connector?
- What sender, subject, or body pattern uniquely identifies `TEXT HELLO` messages?
- Does each Gmail item include the person's name in a consistent place?
- Where should co-host email addresses be sourced from?
- Should the weekly output be a Gmail draft, plain text, or a self-email to Brad?
- Should the co-host receive only names, or also any message/context attached to the `TEXT HELLO` item?
- Are there weeks with multiple co-hosts or no co-host?

## Related Docs

- [Weekly Checklist](weekly-checklist.md)
- [Online Community Response Standards](../people/online-community-response-standards.md)
- [Source Systems](../governance/source-systems.md)
- [Access and Safety](../governance/access-and-safety.md)
- [Online Response Queue Agent](../../agents/ministry/online-response-queue-agent.md)
