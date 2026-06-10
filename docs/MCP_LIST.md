# MCP List

MCP integrations are added one at a time after the required account login or token is ready.

## Required

| Name | Status | Auth |
| --- | --- | --- |
| Filesystem | Defined, disabled | Local permissions |
| Fetch | Defined, disabled | `BLOG_API_TOKEN` |
| Git | Defined, disabled | Git credentials |

## Optional

| Name | Status | Auth |
| --- | --- | --- |
| Playwright | Defined, disabled | Browser session |
| SQLite | Defined, disabled | Local database |
| Google Drive | Defined, disabled | Google OAuth |

The active machine-readable list is stored in `config/mcp.json`.
