# Operation And Logging

Runtime events are written to separate log files.

## Logs

```text
logs/app.log
logs/upload.log
logs/error.log
logs/audit.log
```

## Monitoring Targets

- Analysis success rate: `95%` or higher.
- Upload success rate: `99%` or higher.
- Average processing time: `30` seconds or less.

## Recovery Levels

- Level 1: retry.
- Level 2: notify administrator.
- Level 3: manual handling.

## Retention

- Images: `7` days.
- Markdown: `30` days.
- Logs: `90` days.
