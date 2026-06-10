# Skill System

The skill system chooses blog writing rules from image analysis results.

## Goals

- Select the most relevant writing skill automatically.
- Keep category rules separate from shared blog writing prompts.
- Make the selected skill explainable through matched signals and confidence.
- Fall back to `default.md` when no category is reliable.

## Skill Files

```text
skills/
  restaurant.md
  travel.md
  appliance.md
  product-review.md
  daily.md
  default.md
```

Each skill defines:

- Use cases
- Matching signals
- Writing rules
- Required output sections
- Safety boundaries

## Routing Flow

1. Image analysis returns structured observations.
2. The router compares observations against category signals.
3. The router selects the highest-confidence skill.
4. If confidence is below the threshold, `default.md` is selected.
5. The blog writer prompt receives the image analysis result, selected skill, and category metadata.

## Routing Inputs

Expected image analysis fields:

```json
{
  "mainSubject": "",
  "objects": [],
  "setting": "",
  "textInImage": [],
  "categoryHints": [],
  "keywords": [],
  "confidenceNotes": []
}
```

## Routing Output

Expected skill selection result:

```json
{
  "skill": "restaurant.md",
  "category": "food",
  "confidence": 0.86,
  "matchedSignals": ["plate", "menu", "restaurant table"],
  "fallbackUsed": false
}
```

## Confidence Rules

- `0.80` or higher: select the matched category skill.
- `0.55` to `0.79`: select the matched category skill, but write conservatively.
- Below `0.55`: use `default.md`.

## Current Categories

| Category | Skill | Input Path |
| --- | --- | --- |
| Restaurant | `restaurant.md` | `input/food` |
| Travel | `travel.md` | `input/travel` |
| Appliance | `appliance.md` | `input/appliance` |
| Product Review | `product-review.md` | `input/product-review` |
| Daily | `daily.md` | `input/daily` |

## Selection Priority

1. `restaurant`
2. `travel`
3. `appliance`
4. `product-review`
5. `daily`
6. `default`

When multiple categories match, the first category in the priority list wins.
