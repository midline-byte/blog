# STEP 1. 개발 환경 구성

## 목적

본 프로젝트는 사용자가 업로드한 이미지를 AI가 분석하여 블로그 게시글을 자동 생성하고 블로그 플랫폼에 업로드하는 자동화 시스템 구축을 목표로 한다.

STEP 1에서는 개발 환경 구성 및 AI CLI 도구 연동을 수행한다.

---

# 개발 환경

## 필수 프로그램

| 구분              | 제품           | 용도            |
| --------------- | ------------ | ------------- |
| IDE             | VSCode       | 메인 개발 환경      |
| 형상관리            | Git          | 소스 버전 관리      |
| Runtime         | Node.js LTS  | MCP 및 CLI 실행  |
| Runtime         | Python 3.12+ | 이미지 처리        |
| AI CLI          | Claude Code  | 프로젝트 관리       |
| AI CLI          | Codex CLI    | 코드 생성 및 자동화   |
| Package Manager | npm          | MCP 설치        |
| Package Manager | pip          | Python 패키지 설치 |

---

# 권장 버전

| 항목          | 버전        |
| ----------- | --------- |
| VSCode      | Latest    |
| Node.js     | 22 LTS 이상 |
| Python      | 3.12 이상   |
| Git         | Latest    |
| Claude Code | Latest    |
| Codex CLI   | Latest    |

---

# 프로젝트 디렉토리 구조

```text
blog-ai-project/

├─ docs/
├─ input/
├─ output/
├─ prompts/
├─ skills/
├─ config/
├─ logs/
├─ src/
├─ tests/
├─ .env
├─ .gitignore
└─ README.md
```

---

# 디렉토리 설명

## docs

프로젝트 문서 저장

예시

```text
docs/
 ├─ PROJECT_SETUP.md
 ├─ BLOG_WORKFLOW.md
 └─ MCP_LIST.md
```

## input

원본 이미지 저장

```text
input/
 ├─ food/
 ├─ travel/
 └─ appliance/
```

## output

AI 생성 결과 저장

```text
output/
 ├─ markdown/
 ├─ html/
 └─ images/
```

## prompts

공통 프롬프트 저장

```text
prompts/
 ├─ image-analysis.md
 ├─ blog-writer.md
 └─ seo-generator.md
```

## skills

테마별 블로그 작성 규칙

```text
skills/
 ├─ restaurant.md
 ├─ travel.md
 ├─ appliance.md
 └─ default.md
```

## config

설정 파일 저장

```text
config/
 ├─ blog.json
 ├─ mcp.json
 └─ categories.json
```

## logs

실행 로그 저장

```text
logs/
 ├─ app.log
 ├─ upload.log
 └─ error.log
```

---

# Git 초기화

```bash
git init

git branch -M main

git add .

git commit -m "Initial Project Structure"
```

---

# .gitignore

```gitignore
node_modules/

.venv/

.env

output/

logs/

dist/

coverage/

__pycache__/

*.pyc
```

---

# 환경 변수

## .env

```env
OPENAI_API_KEY=

ANTHROPIC_API_KEY=

BLOG_API_URL=

BLOG_API_TOKEN=

IMAGE_STORAGE_PATH=

LOG_LEVEL=INFO
```

---

# Claude Code 역할

* 프로젝트 구조 생성
* 코드 리팩토링
* MCP 설정 생성
* 문서 생성
* 테스트 코드 생성

---

# Codex CLI 역할

* 기능 구현
* 코드 생성
* 버그 수정
* 테스트 자동화
* 배포 스크립트 작성

---

# STEP 1 체크리스트

* [ ] VSCode 설치
* [ ] Git 설치
* [ ] Node.js 설치
* [ ] Python 설치
* [ ] Claude Code 설치
* [ ] Codex CLI 설치
* [ ] 프로젝트 디렉토리 생성
* [ ] Git 초기화
* [ ] .env 생성
* [ ] README.md 생성

---

# 완료 기준

아래 조건을 모두 만족하면 STEP 1 완료로 간주한다.

1. 개발 환경 설치 완료
2. CLI 도구 설치 완료
3. 프로젝트 구조 생성 완료
4. Git 저장소 초기화 완료
5. 환경 변수 파일 생성 완료

---

# 다음 단계

STEP 2에서는 블로그 테마별 Skill 시스템을 설계한다.

* restaurant.md
* travel.md
* appliance.md
* default.md

각 Skill 파일은 AI가 이미지 분석 결과에 따라 자동 선택하여 블로그 작성 규칙으로 사용한다.
