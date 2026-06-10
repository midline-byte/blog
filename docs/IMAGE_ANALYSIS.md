# Image Analysis Engine

STEP 3 defines the image validation, analysis data contract, category classification, skill mapping, and logging format.

## Processing Flow

```text
Image upload
  -> file validation
  -> image analysis
  -> object and OCR extraction
  -> keyword extraction
  -> category classification
  -> skill selection
  -> blog generation input
```

## Supported Images

- `jpg`
- `jpeg`
- `png`
- `webp`
- `heic`

Maximum file size: `20MB`.

Maximum images per post: `20`.

## Analysis Output

```json
{
  "fileName": "",
  "width": 0,
  "height": 0,
  "objects": [],
  "ocr": [],
  "locationType": "",
  "mood": "",
  "dominantColors": [],
  "keywords": [],
  "category": "",
  "confidence": 0,
  "skill": ""
}
```

## Category Rules

| Category | Signals |
| --- | --- |
| `restaurant` | food, menu, restaurant, coffee, dish, plate, table |
| `travel` | landscape, landmark, beach, hotel, mountain, station, airport |
| `appliance` | tv, air-conditioner, vacuum, washer, refrigerator, appliance |
| `product-review` | product, package, unboxing, brand, label, model |
| `daily` | selected when no category reaches the review threshold |

## Confidence Score

Confidence is expressed as `0` to `100`.

- `90` or higher: auto-select category.
- `70` to `89`: use recommended category.
- Below `70`: needs user review and falls back to `daily`.

## Multiple Images

For a single post, process `1` to `20` images.

Main image priority:

1. people
2. food
3. landmark
4. product

## Error Output

Analysis failure:

```json
{
  "result": "fail",
  "message": "image analysis error"
}
```

Category classification fallback:

```json
{
  "category": "daily",
  "skill": "daily.md"
}
```

## Logs

Success:

```text
[INFO] image analyzed
```

Failure:

```text
[ERROR] image analysis failed
```
