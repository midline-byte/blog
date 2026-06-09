# Blog AI Project

AI image analysis results are used to generate blog posts and prepare upload-ready content.

## Project Structure

```text
docs/      Project documentation
input/     Source images grouped by topic
output/    Generated markdown, HTML, and images
prompts/   Shared AI prompts
skills/    Topic-specific writing rules
config/    Runtime and category configuration
logs/      Runtime logs
src/       Application source code
tests/     Test code
```

## Requirements

- Node.js 22 LTS or newer
- Python 3.12 or newer
- Git
- npm
- pip
- Claude Code
- Codex CLI

## Environment

Copy `.env` values into your local environment before running automation.

Required keys:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `BLOG_API_URL`
- `BLOG_API_TOKEN`
- `IMAGE_STORAGE_PATH`
- `LOG_LEVEL`

## Workflow

1. Add source images under `input/`.
2. Run image analysis.
3. Generate blog content with the selected skill.
4. Save generated artifacts under `output/`.
5. Upload final content to the blog platform.
