# STEP 6. BLOG_PUBLISH_ENGINE.md

## 목적

생성된 게시글을 블로그 플랫폼에 업로드한다.

---

# 지원 플랫폼

## 1. 티스토리

## 2. 워드프레스

## 3. 네이버 블로그

## 4. 자체 CMS

---

# 처리 흐름

```text
Markdown 생성

↓

이미지 업로드

↓

본문 생성

↓

API 호출

↓

게시 완료
```

---

# 업로드 모드

## Draft

임시 저장

## Publish

즉시 발행

---

# 게시글 구성

```json
{
  "title":"",
  "content":"",
  "tags":[]
}
```

---

# 이미지 처리

## 업로드 전

* 리사이징
* 압축
* EXIF 제거

---

# 실패 처리

## 재시도

```text
최대 3회
```

---

# 성공 로그

```json
{
  "status":"success",
  "postId":"1234"
}
```

---

# 실패 로그

```json
{
  "status":"fail",
  "message":"API Error"
}
```

---

# 완료 조건

* 업로드 성공
* URL 저장
* 결과 로그 저장
