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
Use `.env.example` as the committed template and keep real credentials only in `.env`.

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

## Local Image Analysis

```bash
python -m src.analyze_image input/food/sample.png
```

The local analyzer validates image files and applies rule-based category classification. AI Vision integration can replace the observation source while keeping the same output contract.

## Blog Generation

```bash
python -m unittest discover -s tests
```

The current implementation provides local validation, classification, markdown generation, publish payload construction, and operation logging. External AI and blog API calls are connected through environment variables and MCP configuration when credentials are ready.

## Publish

Publishing requires:

- `BLOG_API_URL`
- `BLOG_API_TOKEN`

Without those values, the publish engine returns a structured failure instead of making a network call.
