# Google Calendar Editor [EN](README_EN.md)

通过 Google Calendar API 批量创建日历事件，支持自动去重。

## 前置要求

1. 在 [Google Cloud Console](https://console.cloud.google.com/) 启用 Calendar API，下载 OAuth 凭据保存到 `~/.claude/mcp/google-calendar/credentials.json`
2. 首次运行会打开浏览器进行 OAuth 授权，之后 token 自动缓存在 `~/.claude/mcp/google-calendar/token.json`

## 用法

```bash
python3 scripts/create_events.py --json '[
  {
    "summary": "事件标题",
    "start": "2026-06-01T10:00:00+08:00",
    "end": "2026-06-01T11:00:00+08:00",
    "description": "备注（可选）",
    "tz": "Asia/Shanghai"
  }
]'
```

### 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `summary` | 是 | 事件标题 |
| `start` | 是 | 开始时间，ISO 8601 格式 + 时区偏移 |
| `end` | 是 | 结束时间，格式同上 |
| `description` | 否 | 备注 |
| `tz` | 否 | 时区，默认 Asia/Shanghai |

支持传入 JSON 数组批量创建，重复标题的事件会自动跳过。
