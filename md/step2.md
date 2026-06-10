# STEP 2. Skill 시스템 설계

## 목적

이미지 분석 결과에 따라 적절한 블로그 작성 규칙(Skill)을 자동 선택하여 일관된 품질의 게시글을 생성한다.

---

# Skill 이란

Skill은 특정 주제의 블로그 글을 작성하기 위한 규칙 집합이다.

AI는 이미지 분석 결과를 기반으로 Skill을 선택하고 해당 규칙을 적용하여 글을 생성한다.

---

# Skill 동작 흐름

```text
사용자 이미지 업로드

    ↓

이미지 분석

    ↓

카테고리 분류

    ↓

Skill 선택

    ↓

블로그 글 생성

    ↓

SEO 최적화

    ↓

출력
```

---

# Skill 디렉토리 구조

```text
skills/

├─ restaurant.md
├─ travel.md
├─ appliance.md
├─ product-review.md
├─ daily.md
└─ default.md
```

---

# Skill 선택 규칙

## 맛집

조건

* 음식 사진 존재
* 메뉴판 존재
* 식당 내부 사진 존재
* 음식 비중 50% 이상

선택 Skill

```text
restaurant.md
```

---

## 여행지

조건

* 관광지
* 풍경
* 랜드마크
* 숙소

선택 Skill

```text
travel.md
```

---

## 생활가전

조건

* 전자제품
* 가전제품
* 사용 후기 목적

선택 Skill

```text
appliance.md
```

---

## 제품 리뷰

조건

* 제품 단독 촬영
* 언박싱
* 사용 후기

선택 Skill

```text
product-review.md
```

---

## 일상

조건

* 특정 카테고리 분류 실패

선택 Skill

```text
daily.md
```

---

# Skill 공통 구조

모든 Skill은 동일한 구조를 가진다.

```text
1. 목적
2. 작성 스타일
3. 문체
4. 글 구성
5. SEO 규칙
6. 제목 규칙
7. 태그 규칙
8. 금지 사항
```

---

# Skill 기본 인터페이스

```yaml
category:
description:
writing_style:
tone:
seo:
hashtags:
output_format:
```

---

# AI Skill 선택 우선순위

```text
1. restaurant
2. travel
3. appliance
4. product-review
5. daily
6. default
```

---

# 출력 규격

모든 Skill은 다음 결과를 생성해야 한다.

## 제목

3개 이상

예시

```text
제목 후보 1
제목 후보 2
제목 후보 3
```

---

## 본문

최소 1000자 이상

권장 1500~2500자

---

## 요약

150자 이내

---

## 태그

10개 이상

---

## SEO 키워드

5개 이상

---

# 이미지 활용 규칙

## 단일 이미지

1개의 대표 이미지 사용

---

## 다중 이미지

이미지 순서를 유지

```text
이미지1 → 도입부

이미지2 → 본문1

이미지3 → 본문2

이미지4 → 마무리
```

---

# 예외 처리

## 카테고리 판별 실패

```text
default.md 사용
```

---

## 복합 카테고리

예시

```text
맛집 + 여행지
```

우선순위 적용

```text
restaurant 우선
```

---

# STEP 2 완료 조건

* [ ] skills 디렉토리 생성
* [ ] restaurant.md 생성
* [ ] travel.md 생성
* [ ] appliance.md 생성
* [ ] product-review.md 생성
* [ ] daily.md 생성
* [ ] default.md 생성
* [ ] Skill 선택 로직 정의

---

# 다음 단계

STEP 3에서는 이미지 분석 및 카테고리 분류 엔진을 구현한다.

이미지 분석 결과는 Skill 선택의 입력 데이터로 사용된다.
