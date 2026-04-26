# Online Analytics Reporting

This document defines the online campus responsibility for weekly digital attendance and engagement reporting.

## Purpose

Online analytics reporting exists to give church leadership a consistent weekly picture of how people are engaging with Northridge online.

The immediate recurring responsibility is to report online campus numbers to `jennie.miller@northridgerochester.com`, who prepares weekly multi-campus analytics summaries.

Agent boundary:

- Agents may collect, normalize, summarize, and prepare the report.
- Agents must not email Jennie or anyone else.
- Brad or another approved human sends the final report through the appropriate channel.

## Reporting Goals

- Provide timely weekly online campus numbers.
- Separate source-system facts from estimates or assumptions.
- Avoid double-counting when one stream is distributed through multiple destinations.
- Preserve enough source detail to explain where a number came from.
- Build toward automation without losing human review of ambiguous metrics.

## Current Source Map

### Church Online Platform

Use for:

- Church Online Platform attendance
- unique viewers or attenders
- peak concurrent attenders
- chat participation
- live prayer sessions and prayer requests
- Moment impressions and interactions

Current automation posture:

- Manual admin analytics first.
- Public support docs describe admin analytics, but no public reporting API has been confirmed yet.
- Treat Church Online Platform numbers as platform-attender metrics, not total stream-delivery metrics.

### Resi

Use for:

- stream-delivery analytics from the Resi player or media site
- live and on-demand stream performance
- viewer breakdowns, watch time, geography, device data, and exports when available
- Facebook social analytics if Resi is the approved source for those numbers

Current automation posture:

- Manual export first.
- Resi publicly documents analytics and exports.
- Resi publicly documents a Go Live API, but a public analytics API has not yet been confirmed.
- Verify whether Resi analytics includes Church Online Platform, Triumph mobile app, Apple TV, Roku, and other destinations that use the same Resi stream URL.

### YouTube

Use for:

- YouTube channel and video views
- watch time
- average view duration
- live concurrent viewer metrics when available
- YouTube-specific engagement

Current automation posture:

- Strong API candidate.
- The YouTube Analytics API supports targeted reporting for channel and video metrics.
- Use read-only OAuth scopes.

### Facebook / Meta

Use for:

- Facebook Page live or video performance when it is not already reliably captured by Resi
- Facebook-specific views, minutes viewed, reactions, comments, and shares when needed

Current automation posture:

- Manual export or Resi social analytics first.
- Graph API automation may be possible, but it depends on Page access, permissions, and whether the relevant content is Page video, live video, or crossposted content.
- Treat Facebook numbers as lower-confidence until the collection method is tested.

### Triumph / Rock-Powered Mobile App and TV Apps

Use for:

- mobile app, Apple TV, and Roku viewing only if the source system exposes those numbers directly or if Resi confirms they are included in the same stream analytics.

Current automation posture:

- Unknown.
- The first task is to identify whether these views are counted in Resi, a Triumph admin surface, Rock, or another analytics system.

## Weekly Workflow

### 1. Identify the Reporting Window

- Confirm the service date and week-start date.
- Confirm whether Jennie's report expects Sunday-only numbers, weekend service numbers, or a Monday-through-Sunday week.
- Note any special services, outages, holidays, or streaming changes.

### 2. Collect Source Numbers

Collect from each available source:

- Church Online Platform analytics
- Resi analytics or export
- YouTube Analytics
- Facebook or Meta Business Suite analytics, if needed
- app or TV analytics, if available

For each number, record:

- source system
- source metric name
- value
- date range
- collection method
- confidence level
- notes about known gaps

### 3. Normalize the Report

Translate source metrics into the weekly report fields defined in [Online Analytics Metrics](../dashboards/online-analytics-metrics.md).

Do not combine numbers into a total unless the deduplication logic is understood.

Recommended initial report shape:

- Church Online Platform unique attenders
- Church Online Platform peak concurrent attenders
- Church Online Platform chat participants
- Resi stream viewers or views
- YouTube views
- Facebook views, if available
- app and TV views, if available
- notes and confidence flags

### 4. Reconcile and Flag Ambiguity

Before sending, ask:

- Are these numbers counting people, browsers, sessions, video starts, or views?
- Does Resi already include the app or Church Online Platform traffic?
- Is YouTube included in Resi, or does it need to be reported separately?
- Is Facebook included in Resi, or does it need to be reported separately?
- Are on-demand views included, excluded, or reported separately?

### 5. Prepare Jennie's Summary

Prepare a short, human-readable report with:

- the date or week covered
- the numbers requested by Jennie
- any caveats that affect comparison
- one sentence if the methodology changed

Brad or another approved human sends the report.

### 6. Store the Durable Record

Store normalized weekly values in a local structured file or future dashboard table.

Do not store:

- API tokens
- raw exports with unnecessary private data
- screenshots containing irrelevant account details
- credentials or admin URLs that should stay private

## Automation Roadmap

### Stage 1: Manual but Structured

- Use the `tools/analytics` weekly JSON format.
- Produce a repeatable weekly summary.
- Identify which fields Jennie actually needs.

### Stage 2: Export-Assisted

- Standardize Resi and Church Online Platform export handling if exports are available.
- Add CSV parsers for repeatable export formats.
- Keep manual entry for sources without API access.

### Stage 3: API-Assisted

- Add a YouTube Analytics read-only connector.
- Investigate whether Church Online Platform has a private or partner API.
- Investigate whether Resi analytics can be exported programmatically.
- Test Meta Graph API only after Page permissions and metric definitions are clear.

### Stage 4: Reviewed Automation

- Generate Jennie's weekly summary automatically.
- Keep a human approval step before anything is sent.
- Add data-health checks for missing sources, unusual drops, duplicate counting, and methodology changes.

## Open Questions

- What exact deadline and channel does Jennie expect each week?
- Which fields does Jennie currently enter into the multi-campus report?
- Is the report Sunday-service-only or full-week online engagement?
- Does Resi include Church Online Platform views when Church Online Platform embeds the Resi player?
- Does Resi include Triumph app, Apple TV, and Roku app viewing?
- Does Resi include YouTube and Facebook social destinations in the same export, or should those remain separate?
- Which number should leadership treat as the headline online attendance number?
- Should on-demand views be included in the weekly attendance report or tracked separately?

## Related Files

- [Online Analytics Metrics](../dashboards/online-analytics-metrics.md)
- [Success Metrics](../vision/success-metrics.md)
- [Weekly Checklist](weekly-checklist.md)
- [Technical Systems](technical-systems.md)
- [Analytics tool README](../../tools/analytics/README.md)
