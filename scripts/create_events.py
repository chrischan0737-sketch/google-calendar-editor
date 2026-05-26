#!/usr/bin/env python3
"""Google Calendar 事件创建工具 — 支持批量创建与去重"""

import os, sys, json, argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
BASE = os.path.expanduser("~/.claude/mcp/google-calendar")
CREDENTIALS_FILE = os.path.join(BASE, "credentials.json")
TOKEN_FILE = os.path.join(BASE, "token.json")

def get_events(args):
    if args.json:
        data = json.loads(args.json)
    elif not sys.stdin.isatty():
        data = json.load(sys.stdin)
    else:
        return None
    return data if isinstance(data, list) else [data]

def get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            pass
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        if not os.path.exists(CREDENTIALS_FILE):
            print("Error: credentials.json not found at", CREDENTIALS_FILE, file=sys.stderr)
            sys.exit(1)
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

def create(service, events, calendar="primary"):
    times = [e["start"] for e in events] + [e["end"] for e in events]
    existing = service.events().list(
        calendarId=calendar, timeMin=min(times), timeMax=max(times),
    ).execute().get("items", [])
    existing_titles = {e.get("summary") for e in existing}
    created, skipped = 0, 0
    for ev in events:
        if ev["summary"] in existing_titles:
            print(f"  ↺ Skipped (exists): {ev['summary']}")
            skipped += 1
            continue
        tz = ev.get("tz", "Asia/Shanghai")
        body = {
            "summary": ev["summary"],
            "description": ev.get("description", ""),
            "start": {"dateTime": ev["start"], "timeZone": tz},
            "end": {"dateTime": ev["end"], "timeZone": tz},
            "reminders": {"useDefault": True},
        }
        service.events().insert(calendarId=calendar, body=body).execute()
        print(f"  ✓ Created: {ev['summary']}")
        created += 1
    print(f"\nDone: {created} created, {skipped} skipped")
    return created, skipped

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Create Google Calendar events")
    p.add_argument("--json", help="JSON event(s) string")
    args = p.parse_args()
    events = get_events(args)
    if not events:
        print("Usage: provide events via --json or pipe JSON stdin", file=sys.stderr)
        sys.exit(1)
    create(get_service(), events)
