# STEP 7. OPERATION_AND_LOGGING.md

## 목적

운영 환경에서 발생하는 모든 이벤트를 기록하고 장애를 추적한다.

---

# 로그 구조

```text
logs/

app.log

upload.log

error.log

audit.log
```

---

# app.log

일반 실행 로그

예시

```text
[INFO]

Image Uploaded
```

---

# upload.log

게시글 업로드 로그

예시

```text
[INFO]

Blog Published

Post ID: 1001
```

---

# error.log

오류 로그

예시

```text
[ERROR]

API Timeout
```

---

# audit.log

감사 로그

예시

```text
User Uploaded Image

Generated Blog

Published Blog
```

---

# 모니터링 항목

## 분석 성공률

목표

```text
95% 이상
```

---

## 업로드 성공률

목표

```text
99% 이상
```

---

## 평균 처리 시간

목표

```text
30초 이하
```

---

# 장애 대응

## Level 1

재시도

## Level 2

관리자 알림

## Level 3

수동 처리

---

# 백업 정책

## 이미지

7일

## Markdown

30일

## 로그

90일

---

# 알림

## Slack

## Email

## Discord

---

# 운영 체크리스트

* [ ] 로그 기록
* [ ] 업로드 결과 저장
* [ ] 오류 추적 가능
* [ ] 재시도 가능
* [ ] 관리자 알림 가능

---

# 최종 프로젝트 완료 조건

* STEP 1 환경 구축 완료
* STEP 2 Skill 시스템 완료
* STEP 3 이미지 분석 완료
* STEP 4 글 생성 완료
* STEP 5 MCP 연동 완료
* STEP 6 블로그 업로드 완료
* STEP 7 운영 및 로그 체계 완료

---

# 최종 자동화 흐름

```text
사진 업로드

↓

이미지 분석

↓

카테고리 분류

↓

Skill 선택

↓

블로그 생성

↓

SEO 생성

↓

Markdown 저장

↓

이미지 최적화

↓

블로그 업로드

↓

URL 저장

↓

로그 기록
```
