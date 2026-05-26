---
name: google-calendar-editor
description: >-
  Creates calendar events on Google Calendar via the Calendar API. Triggers when the user mentions 谷歌日历,
  Google Calendar, 写入日历, 创建日历事件, 加到日历, 考试安排, 日程, "add to calendar", "create an event",
  or any request involving writing events/dates to Google Calendar. Use this whenever the user wants to
  put something on their calendar.
---

# Google Calendar Editor

Creates one or more events on the user's Google Calendar via the Calendar API, with automatic duplicate detection.

## Prerequisites

The first run will open a browser for OAuth authentication. After that, the token is cached in `~/.claude/mcp/google-calendar/token.json`.

Credentials file: `~/.claude/mcp/google-calendar/credentials.json`

## Usage

Run the script via Python, passing events as JSON:

```bash
python3 ~/.claude/skills/google-calendar-editor/scripts/create_events.py --json '[
  {"summary": "Event Title", "start": "2026-06-01T10:00:00+08:00", "end": "2026-06-01T11:00:00+08:00", "description": "optional note"}
]'
```

### Event JSON fields

| Field | Required | Description |
|-------|----------|-------------|
| `summary` | Yes | Event title |
| `start` | Yes | Start time in ISO 8601 with tz offset: `2026-06-25T14:30:00+08:00` |
| `end` | Yes | End time in same format |
| `description` | No | Optional notes/description |
| `tz` | No | Timezone override (default: Asia/Shanghai) |

### Batch creation

Pass multiple events in the JSON array to create them all at once. The script automatically detects and skips events with titles that already exist in the target time range.

### Timezone format

Always use `+08:00` suffix for Beijing time (Asia/Shanghai). Example: `2026-07-03T14:30:00+08:00`.

## Example

```bash
python3 ~/.claude/skills/google-calendar-editor/scripts/create_events.py --json '[
  {"summary": "Meeting with Team", "start": "2026-06-01T10:00:00+08:00", "end": "2026-06-01T11:00:00+08:00"}
]'
```
