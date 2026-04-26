# Online Analytics Data

This folder is for structured weekly online analytics records.

Use the analytics toolkit to create a weekly JSON file:

```bash
python3 tools/analytics/analytics_cli.py new-week \
  --week-start 2026-04-19 \
  --output data/online-analytics/2026-04-19.json
```

Do not store credentials, raw sensitive exports, cookies, OAuth tokens, or unnecessary account details here.

Weekly records should preserve:

- source system
- source metric name
- reported value
- collection method
- confidence level
- methodology notes
- missing sources

The first goal is consistent reporting. Automation can grow once the source-system definitions are stable.
