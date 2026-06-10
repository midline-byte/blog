# Image Analysis Prompt

Analyze the provided image and return structured observations suitable for blog writing.

Include:

- Main subject
- Visible objects
- Location or setting clues
- Mood and tone
- Product, food, travel, or appliance category hints
- SEO keyword candidates

Return JSON with this shape:

```json
{
  "mainSubject": "",
  "objects": [],
  "setting": "",
  "textInImage": [],
  "mood": "",
  "categoryHints": [],
  "keywords": [],
  "confidenceNotes": []
}
```
