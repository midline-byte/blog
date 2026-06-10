# MCP Architecture

MCP integrations are configured incrementally and only enabled after the required account login or API token is ready.

## Required MCP

| MCP | Purpose | Auth |
| --- | --- | --- |
| Filesystem | Read images, save markdown, write logs | Local permissions |
| Fetch | Blog API calls and authenticated REST requests | Blog API token |
| Git | Commit and version tracking | Git credentials |

## Optional MCP

| MCP | Purpose | Auth |
| --- | --- | --- |
| Playwright | Browser automation and admin-page upload | Browser session |
| SQLite | Post history and duplicate prevention | Local database |
| Google Drive | Image backup | Google OAuth |

## Security

- Never hardcode API keys or tokens.
- Store credentials in `.env` or provider-specific secret storage.
- Add MCP servers one at a time after login is complete.
- Do not store personal data, unencrypted secrets, or raw credential dumps.
