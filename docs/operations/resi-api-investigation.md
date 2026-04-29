# Resi API Investigation

This note captures what was learned while testing whether the online analytics reporting agent can fetch Resi analytics programmatically.

Investigation date: 2026-04-26

## Purpose

The question was whether a dedicated Resi API client can support weekly online analytics reporting, especially views, unique viewers, watch time, peak concurrent viewers, and other Studio analytics used for ministry reporting.

## API Client Created

A dedicated API client was created in Resi Studio.

- Client name: `ONL Analytics Reporting - Read Only`
- Client role: `Resi On Demand API`
- Intended use: online analytics/reporting support for this repo

Do not commit the client ID, client secret, access tokens, cookies, or browser session tokens.

## Public References Checked

- Resi API basics support article: `https://support.pushpay.com/s/article/Resi-API-Basics?type=resi`
- Resi Swagger UI: `https://api.resi.io/docs`
- Resi OpenAPI JSON: `https://api.resi.io/docs/v3/api-docs`

The support article points to the Swagger site, explains client-credentials OAuth, and uses `https://api.resi.io/v1/ondemand/playlists` as an example endpoint.

## Confirmed OAuth Flow

The public API token endpoint is:

```text
https://api.resi.io/v1/oauth/token
```

Use the OAuth `client_credentials` grant with the API client ID and secret. The tested request sent the client credentials in the request body as form data.

Observed result:

- Token request succeeded with HTTP `200`
- Response included an access token
- Response included `expires_in=21600`

Do not print the access token in logs.

## Confirmed Public API Access

Using the bearer token from the public OAuth endpoint, this endpoint succeeded:

```text
GET https://api.resi.io/v1/ondemand/playlists
```

Observed result:

- HTTP `200`
- Response shape: JSON array
- Playlist count at test time: `20`
- Playlist fields included `id`, `name`, `size`, `thumbnail`, and `url`

This proves that the API client works for the public Resi On Demand API surface.

## Public OpenAPI Surface

The public OpenAPI spec listed only these endpoint groups:

- OAuth Authentication
- On Demand
- Go Live Schedules
- Encoders
- Destination Groups

Endpoints observed:

```text
POST /v1/oauth/token
GET  /v1/ondemand/playlists
GET  /v1/ondemand/playlists/{playlistId}
GET  /v1/ondemand/videos/{videoId}
GET  /v1/encoders
GET  /v1/destinationgroups
GET  /v1/schedules/{scheduleId}
POST /v1/schedules/live
POST /v1/schedules/{scheduleId}/stop
```

No public endpoint was found for analytics, statistics, views, viewers, watch time, KPIs, reports, or exports.

## Studio Analytics Clue

Resi Studio appears to load analytics through internal telemetry endpoints, including KPI and export-style routes under `telemetry.resi.io`.

On 2026-04-26, the open Resi Studio analytics page was:

```text
https://studio.resi.io/analytics
```

The page showed Northridge Church Event Analytics with these visible controls and concepts:

- date range filters
- event list filter
- destination tabs such as `Embed Player`, `Stream URL`, and `Facebook`
- group-by options such as none and device type
- day/week/month aggregation
- export buttons in the UI
- viewer breakdowns by city/location

For the visible range `04/20/2026` through `04/26/2026`, with `Stream URL` selected, the page displayed:

- Total viewers: `243`
- Unique viewers: `242`
- Total time watched: `126 hours`
- New viewers: `208`
- Return viewers: `34`

These values are useful examples of the reporting surface, not a stored weekly report.

## Studio Telemetry Endpoints Observed

The Studio page made successful browser-session requests to telemetry endpoints such as:

```text
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/newViewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/returnViewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/totalTimeWatched
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/uniqueViewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/avgWatchTime
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/medianWatchTime
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/peakConcurrentViewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/kpis/views
GET https://telemetry.resi.io/api/v1/customers/{customerId}/webevents/statistics/day/viewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/webevents/statistics/viewers/city
GET https://telemetry.resi.io/api/v1/customers/{customerId}/webevents/statistics/viewers/locations
GET https://telemetry.resi.io/api/v1/customers/{customerId}/contentLibrary/statistics/summary
GET https://telemetry.resi.io/api/v1/customers/{customerId}/contentLibrary/statistics/day/viewers
GET https://telemetry.resi.io/api/v1/customers/{customerId}/contentLibrary/statistics/viewers/city
GET https://telemetry.resi.io/api/v1/customers/{customerId}/contentLibrary/statistics/viewers/locations
```

Observed query parameters included:

- `startDate`
- `endDate`
- `destinationType`, including `embed` and `stream_url`
- `segmentBy`
- `eventAnalytics`
- `isFullMonth`
- `viewAllData`

Important boundary:

- These Studio analytics endpoints appear tied to a signed-in Studio browser session.
- The public API client token is not confirmed to authorize telemetry analytics endpoints.
- Do not build automation around browser session cookies or internal Studio tokens without explicit approval and a supportable security plan.
- Treat endpoint names as vendor-discovery context, not as an approved integration contract.

## Current Conclusion

The Resi API client is useful for public Resi metadata and control surfaces, especially On Demand playlists/videos and Go Live-related resources.

It is not currently proven useful for weekly analytics reporting. Based on the public OpenAPI spec, Resi analytics should remain `manual_ui` or `confirmed_export` until Pushpay/Resi confirms an official analytics API or export endpoint for API clients.

## Reporting Implications

For the online analytics reporting agent:

- Use the Resi public API only for media metadata enrichment unless a supported analytics endpoint is confirmed.
- Do not count Resi API access as `confirmed_api` for analytics metrics.
- Treat Resi analytics values as `manual_ui` or `confirmed_export`.
- Keep YouTube Analytics as the strongest first API candidate.
- Consider a Resi export parser before attempting a Resi analytics connector.

## Support Question To Ask

Ask Resi/Pushpay support:

```text
We created an OAuth API client with Resi On Demand API access. Does Resi offer API access to Studio analytics, including views, unique viewers, average/median watch time, total time watched, peak concurrent viewers, and content-library exports? If so, what API role or endpoint should we use?
```

## Environment Notes

Useful non-secret environment fields:

```text
RESI_API_CLIENT_NAME="ONL Analytics Reporting - Read Only"
RESI_API_CLIENT_ROLES=Resi On Demand API
RESI_API_BASE_URL=https://api.resi.io
RESI_OAUTH_TOKEN_URL=https://api.resi.io/v1/oauth/token
RESI_CLIENT_ID=
RESI_CLIENT_SECRET=
```

The local `.env` may include unquoted values with spaces. Tools should parse `.env` defensively instead of assuming it can always be sourced by a shell.
