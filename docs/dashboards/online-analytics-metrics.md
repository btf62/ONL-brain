# Online Analytics Metrics

This document defines the first-pass metric model for online campus analytics reporting.

The goal is not to force every platform into one misleading number. The goal is to preserve source-system meaning while producing a useful weekly report.

## Metric Principles

- Keep source metrics and normalized metrics separate.
- Record the collection method for every number.
- Prefer platform-specific truth over vague totals.
- Do not deduplicate until the distribution path is verified.
- Treat methodology changes as report notes, not hidden cleanup.

## Confidence Levels

Use one of these confidence levels for each reported number:

- `confirmed_api`: collected through a tested read-only API
- `confirmed_export`: collected from a repeatable export
- `manual_ui`: copied from a known admin screen
- `estimated`: derived from another number or source
- `unknown`: source or definition has not been confirmed

## Source Metrics

Source metrics should be stored as close as possible to the system's own language.

Suggested fields:

- `week_start`
- `service_date`
- `service_label`
- `source_system`
- `source_metric`
- `source_value`
- `source_date_range`
- `collection_method`
- `confidence`
- `collected_at`
- `notes`

## Normalized Weekly Fields

These are candidate normalized fields for the weekly report.

### Church Online Platform

- `church_online_attendance`
- `church_online_unique_viewers`
- `church_online_peak_concurrent`
- `church_online_average_time_attended_minutes`
- `church_online_public_chat_participants`
- `church_online_public_chat_messages`
- `church_online_prayer_requests`
- `church_online_prayer_sessions`
- `church_online_moment_interactions`

### Resi

- `resi_live_viewers`
- `resi_live_views`
- `resi_peak_concurrent`
- `resi_average_watch_time_minutes`
- `resi_total_watch_time_minutes`
- `resi_on_demand_views`
- `resi_facebook_views`
- `resi_export_url_or_reference`

### YouTube

- `youtube_views`
- `youtube_estimated_minutes_watched`
- `youtube_average_view_duration_seconds`
- `youtube_peak_concurrent_viewers`
- `youtube_average_concurrent_viewers`
- `youtube_video_id`
- `youtube_channel_id`

### Facebook / Meta

- `facebook_video_views`
- `facebook_minutes_viewed`
- `facebook_three_second_views`
- `facebook_reactions`
- `facebook_comments`
- `facebook_shares`
- `facebook_video_or_post_id`

### App and TV

- `mobile_app_views`
- `apple_tv_views`
- `roku_views`
- `app_tv_source_system`

Use these only after the source system is confirmed.

### Report-Level Fields

- `headline_online_attendance`
- `headline_online_attendance_method`
- `total_known_platform_views`
- `total_known_platform_views_method`
- `methodology_notes`
- `missing_sources`
- `data_quality_flags`

## Initial Jennie Report Shape

Until the exact multi-campus report fields are confirmed, prepare this concise report:

| Field | Source | Confidence |
| --- | --- | --- |
| Church Online Platform unique attenders | Church Online Platform | manual_ui |
| Church Online Platform peak concurrent | Church Online Platform | manual_ui |
| Church Online Platform chat participants | Church Online Platform | manual_ui |
| Resi stream views/viewers | Resi | confirmed_export or manual_ui |
| YouTube views | YouTube | confirmed_api or manual_ui |
| Facebook views | Resi, Meta Business Suite, or Graph API | manual_ui or unknown |
| App and TV views | Resi, Triumph, or unknown | unknown |
| Notes | Human review | manual_ui |

## Data Quality Flags

Use these flags when preparing a report:

- `missing_source`
- `source_export_failed`
- `metric_definition_changed`
- `possible_double_count`
- `source_includes_multiple_destinations`
- `manual_entry_needed`
- `unusual_change_from_prior_week`
- `special_service_or_holiday`
- `streaming_incident`

## Deduplication Posture

Do not deduplicate across platforms yet.

The likely future model is:

- Church Online Platform measures attendance within the Church Online experience.
- Resi measures stream delivery across destinations that use Resi.
- YouTube measures YouTube-native viewing.
- Facebook measures Facebook-native viewing.
- App and TV viewing may be part of Resi or may need separate reporting.

Until this is verified, report platform-specific numbers and include a caveat rather than claiming one total online audience.
