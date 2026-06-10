# Blog Generation Engine

The blog generation engine converts image analysis results and selected skill rules into upload-ready markdown.

## Inputs

- Image analysis result
- Selected skill file
- User settings such as tone, length, and SEO mode

## Output

Markdown is saved under `output/markdown/` with this pattern:

```text
YYYYMMDD-title.md
```

## Validation Rules

- Generate at least five title candidates.
- Keep titles at 35 characters or fewer when possible.
- Remove duplicate titles.
- Keep each paragraph at 500 characters or fewer.
- Remove advertising-style exaggeration and unsupported claims.
- Generate at least five SEO keywords.
- Generate at least ten hashtags.
