# Online Analytics Toolkit

This folder is the automation workspace for online campus analytics reporting.

The first version is intentionally modest: it creates a structured weekly record and turns that record into a draft summary for human review. API connectors can be added after the source definitions and credentials are clear.

## Commands

Show help:

```bash
python3 tools/analytics/analytics_cli.py --help
```

Create a weekly record:

```bash
python3 tools/analytics/analytics_cli.py new-week \
  --week-start 2026-04-19 \
  --output data/online-analytics/2026-04-19.json
```

Validate a weekly record:

```bash
python3 tools/analytics/analytics_cli.py validate \
  data/online-analytics/2026-04-19.json
```

Print a draft report:

```bash
python3 tools/analytics/analytics_cli.py summarize \
  data/online-analytics/2026-04-19.json
```

## Current Data Flow

1. Create a weekly JSON file.
2. Manually enter the numbers collected from each source.
3. Validate the file.
4. Generate a draft summary.
5. Brad or another approved human sends the final report.

The tool does not send email.

## Future Connectors

Likely connector order:

1. YouTube Analytics API read-only connector.
2. Resi export parser.
3. Church Online Platform export or admin-screen helper, if a supported export path exists.
4. Meta/Facebook connector only after Page permissions and metric definitions are confirmed.
5. Triumph/app/TV connector after the source of those metrics is identified.

## Configuration

Use `config.example.json` as a non-secret template. Real credentials belong in `.env` or a local ignored file, never in this repo.
