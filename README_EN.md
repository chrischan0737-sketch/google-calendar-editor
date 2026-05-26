# Google Calendar Editor

Batch create calendar events on Google Calendar via the Calendar API, with automatic duplicate detection.

## Prerequisites

1. Enable the **Calendar API** in [Google Cloud Console](https://console.cloud.google.com/), download OAuth credentials and save to `~/.claude/mcp/google-calendar/credentials.json`
2. The first run will open a browser for OAuth authorization. After that, the token is automatically cached in `~/.claude/mcp/google-calendar/token.json`

## Usage

```bash
python3 scripts/create_events.py --json '[
  {
    "summary": "Event Title",
    "start": "2026-06-01T10:00:00+08:00",
    "end": "2026-06-01T11:00:00+08:00",
    "description": "Optional note",
    "tz": "Asia/Shanghai"
  }
]'
```

### Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `summary` | Yes | Event title |
| `start` | Yes | Start time, ISO 8601 format with timezone offset |
| `end` | Yes | End time, same format as start |
| `description` | No | Optional notes |
| `tz` | No | Timezone, defaults to Asia/Shanghai |

Supports batch creation by passing a JSON array. Events with duplicate titles are automatically skipped.
