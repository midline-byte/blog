# Blog Workflow

1. Store original images in `input/<category>/`.
2. Analyze image content with AI.
3. Select the matching skill file from `skills/`.
4. Generate a markdown draft under `output/markdown/`.
5. Convert or render HTML under `output/html/`.
6. Store generated or processed images under `output/images/`.
7. Upload the final post to the blog platform.

## End-To-End Pipeline

The final automated flow is:

```text
Image upload
  -> image analysis
  -> category classification
  -> skill selection
  -> blog generation
  -> SEO generation
  -> markdown save
  -> image preparation
  -> blog upload
  -> URL save
  -> logging
```

Local pipeline entry point:

```bash
python -m src.pipeline
```

## Skill Selection

Skill selection uses `config/categories.json` and `config/skill-routing.json`.

The current priority is:

1. `restaurant`
2. `travel`
3. `appliance`
4. `product-review`
5. `daily`
6. `default`
