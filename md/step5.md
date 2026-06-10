# STEP 5. MCP_ARCHITECTURE.md

## 목적

Claude Code 및 Codex CLI가 외부 시스템과 안전하게 통신할 수 있도록 MCP 구성을 정의한다.

---

# MCP 구성도

```text
Claude/Codex

↓

Filesystem MCP

↓

Image Analysis

↓

Blog Engine

↓

Blog API
```

---

# 필수 MCP

## Filesystem MCP

용도

```text
이미지 읽기

Markdown 저장

로그 저장
```

---

## Fetch MCP

용도

```text
REST API 호출

블로그 업로드

인증 처리
```

---

## Git MCP

용도

```text
자동 Commit

버전 관리
```

---

# 선택 MCP

## Playwright MCP

용도

```text
브라우저 자동화

관리자 페이지 업로드
```

---

## SQLite MCP

용도

```text
게시글 이력 관리

중복 업로드 방지
```

---

## Google Drive MCP

용도

```text
이미지 백업
```

---

# 보안 정책

## 금지

```text
API Key 하드코딩

개인정보 저장

비암호화 저장
```

---

# 환경 변수

```env
BLOG_API_URL=
BLOG_API_TOKEN=
```

---

# 완료 조건

* MCP 목록 확정
* 인증 방식 정의
* 보안 정책 정의
