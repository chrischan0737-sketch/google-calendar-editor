# Google Calendar Editor  
[EN](./README_EN.md)

一款通过 Google Calendar API 批量创建日历事件的 SKILL 。支持自动去重，支持各类 AI Agent (Claude Code,Codex等)。


## 一键安装
复制下方提示词直接丢给你的 Agent 就好

```帮我安装google-calendar-editor。请把 https://github.com/chrischan0737-sketch/google-calendar-editor 克隆到~/.claude/skills/google-calendar-editor,安装完成后检查 SKILL.md 和 create_events.py 是否存在，然后安装依赖并验证 create_events.py 可运行。以后我说“添加到我的日历” 类似的话就调用这个skill```


## 使用示例
<img width="1278" height="176" alt="exmp1" src="https://github.com/user-attachments/assets/0b336132-706e-4ab1-93ab-5b457fe106eb" />
<img width="1010" height="414" alt="exmp2" src="https://github.com/user-attachments/assets/e8a11033-b769-48ff-9381-e0ad50224e91" />



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
