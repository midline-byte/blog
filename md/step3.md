# STEP 3. 이미지 분석 및 카테고리 분류 엔진

## 목적

사용자가 업로드한 이미지를 분석하여 이미지의 특징을 추출하고 적절한 블로그 카테고리를 자동으로 선택한다.

본 단계의 결과는 Skill 선택 및 블로그 글 생성의 입력 데이터로 사용된다.

---

# 처리 흐름

```text
이미지 업로드

    ↓

파일 검증

    ↓

이미지 분석

    ↓

객체 인식

    ↓

키워드 추출

    ↓

카테고리 분류

    ↓

Skill 선택

    ↓

글 생성 엔진 전달
```

---

# 입력 데이터

## 지원 확장자

```text
jpg
jpeg
png
webp
heic
```

---

# 파일 검증

## 검증 항목

### 파일 존재 여부

```text
파일 누락 시 오류 반환
```

### 파일 크기

```text
최대 20MB
```

### 이미지 형식

```text
지원 형식 여부 확인
```

### 이미지 손상 여부

```text
이미지 읽기 가능 여부 검사
```

---

# 이미지 분석

## AI 분석 항목

### 객체

예시

```json
{
  "objects": [
    "food",
    "coffee",
    "table",
    "person"
  ]
}
```

---

### 장소

예시

```json
{
  "location_type": "restaurant"
}
```

---

### 분위기

예시

```json
{
  "mood": "cozy"
}
```

---

### 색상

예시

```json
{
  "dominant_colors": [
    "#FFFFFF",
    "#333333"
  ]
}
```

---

### OCR

텍스트가 존재하는 경우 추출

예시

```json
{
  "ocr": [
    "아메리카노",
    "카페라떼"
  ]
}
```

---

# 추출 데이터 모델

```json
{
  "fileName": "",
  "width": 0,
  "height": 0,
  "objects": [],
  "ocr": [],
  "locationType": "",
  "keywords": [],
  "category": "",
  "confidence": 0
}
```

---

# 카테고리 분류 규칙

## 맛집

조건

```text
food 존재

또는

menu 존재

또는

restaurant 존재
```

분류 결과

```text
restaurant
```

---

## 여행지

조건

```text
landscape

landmark

beach

hotel

mountain
```

분류 결과

```text
travel
```

---

## 생활가전

조건

```text
tv

air-conditioner

vacuum

washer

refrigerator
```

분류 결과

```text
appliance
```

---

## 제품 리뷰

조건

```text
product

package

unboxing
```

분류 결과

```text
product-review
```

---

## 일상

조건

```text
위 조건 모두 실패
```

분류 결과

```text
daily
```

---

# 신뢰도 평가

## Confidence Score

범위

```text
0 ~ 100
```

---

## 기준

### 90 이상

```text
자동 선택
```

### 70 ~ 89

```text
추천 카테고리 사용
```

### 70 미만

```text
사용자 검토 필요
```

---

# 다중 이미지 처리

## 동일 게시글

```text
1 ~ 20장 지원
```

---

## 대표 이미지 선정

우선순위

```text
1. 얼굴
2. 음식
3. 랜드마크
4. 제품
```

---

# OCR 활용

## 맛집

메뉴명 추출

예시

```text
아메리카노
파스타
등심 스테이크
```

---

## 여행지

장소명 추출

예시

```text
남산타워
에펠탑
후지산
```

---

## 제품

모델명 추출

예시

```text
LG OLED C4
Galaxy S26
```

---

# 출력 예시

```json
{
  "category": "restaurant",
  "confidence": 96,
  "keywords": [
    "파스타",
    "레스토랑",
    "점심",
    "맛집"
  ],
  "skill": "restaurant.md"
}
```

---

# 오류 처리

## 이미지 분석 실패

```json
{
  "result": "fail",
  "message": "image analysis error"
}
```

---

## 카테고리 판별 실패

```json
{
  "category": "default",
  "skill": "default.md"
}
```

---

# 로그 기록

## 분석 성공

```text
[INFO]
image analyzed
```

---

## 분석 실패

```text
[ERROR]
image analysis failed
```

---

# STEP 3 완료 조건

* [ ] 이미지 검증 모듈 정의
* [ ] 객체 인식 규칙 정의
* [ ] OCR 규칙 정의
* [ ] 카테고리 분류 규칙 정의
* [ ] Confidence Score 정의
* [ ] Skill 매핑 정의
* [ ] 로그 규격 정의

---

# 다음 단계

STEP 4에서는 실제 블로그 글 생성 엔진을 설계한다.

입력

* 이미지 분석 결과
* Skill 파일
* 사용자 설정

출력

* 제목
* 본문
* 태그
* SEO 키워드
* 요약문
* 업로드용 Markdown

```
```
