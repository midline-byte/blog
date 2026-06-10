# Blog Publish Engine

The publish engine sends generated markdown to a blog platform in draft or publish mode.

## Supported Platforms

- Tistory
- WordPress
- Naver Blog
- Custom CMS

## Flow

```text
Markdown generated
  -> images prepared
  -> post payload built
  -> API request sent
  -> result logged
```

## Modes

- `draft`: save as draft.
- `publish`: publish immediately.

## Result Format

Success:

```json
{
  "status": "success",
  "postId": "1234",
  "url": ""
}
```

Failure:

```json
{
  "status": "fail",
  "message": "API Error"
}
```
