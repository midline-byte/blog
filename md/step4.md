# STEP 4. BLOG_GENERATION_ENGINE.md

## 목적

이미지 분석 결과와 Skill 규칙을 이용하여 SEO 최적화된 블로그 게시글을 생성한다.

---

# 입력 데이터

## 이미지 분석 결과

```json
{
  "category": "restaurant",
  "keywords": [
    "파스타",
    "스테이크",
    "레스토랑"
  ]
}
```

## Skill 파일

```text
skills/restaurant.md
```

## 사용자 설정

```json
{
  "tone":"friendly",
  "length":"long",
  "seo":true
}
```

---

# 생성 순서

```text
이미지 분석 결과

↓

Skill 선택

↓

제목 생성

↓

본문 생성

↓

SEO 키워드 생성

↓

태그 생성

↓

요약 생성

↓

Markdown 저장
```

---

# 제목 생성 규칙

개수

```text
최소 5개
```

조건

```text
SEO 키워드 포함

35자 이내

클릭 유도형 금지
```

---

# 본문 구조

## 도입

방문 계기

## 본문

분위기

특징

장점

단점

추천 대상

## 마무리

총평

---

# 본문 길이

| 유형     | 글자수  |
| ------ | ---- |
| Short  | 1000 |
| Medium | 2000 |
| Long   | 3000 |

---

# SEO 생성

최소 5개

예시

```text
강남맛집
파스타맛집
스테이크추천
데이트맛집
강남레스토랑
```

---

# 태그 생성

최소 10개

예시

```text
#강남맛집
#파스타
#스테이크
```

---

# 출력 파일

```text
output/markdown/

YYYYMMDD-title.md
```

---

# 품질 검증

* 제목 중복 금지
* 문단 길이 500자 이하
* 광고성 표현 제거
* 과장 표현 제거

---

# 완료 조건

* 제목 생성 가능
* 본문 생성 가능
* SEO 생성 가능
* 태그 생성 가능
* Markdown 저장 가능
