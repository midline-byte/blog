# Blog Workflow

1. Store original images in `input/<category>/`.
2. Analyze image content with AI.
3. Select the matching skill file from `skills/`.
4. Generate a markdown draft under `output/markdown/`.
5. Convert or render HTML under `output/html/`.
6. Store generated or processed images under `output/images/`.
7. Upload the final post to the blog platform.

## Skill Selection

Skill selection uses `config/categories.json` and `config/skill-routing.json`.

The current priority is:

1. `restaurant`
2. `travel`
3. `appliance`
4. `product-review`
5. `daily`
6. `default`
