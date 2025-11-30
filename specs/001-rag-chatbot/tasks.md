# Tasks: Context-Aware RAG Chatbot

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit test tasks requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/` (FastAPI)
- **Frontend**: `physical-ai-book/src/` (Docusaurus/React)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure (`backend/app/`, `backend/tests/`, `backend/app/api`, `backend/app/core`, `backend/app/db`, `backend/app/services`)
- [x] T002 Initialize Python environment and create `backend/requirements.txt` with dependencies (fastapi, uvicorn, openai, qdrant-client, asyncpg, sqlalchemy, python-dotenv)
- [x] T003 [P] Create `backend/.env` template with placeholders for OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL
- [x] T004 [P] Create `backend/app/core/config.py` to load environment variables using pydantic-settings
- [x] T005 Create `backend/app/main.py` with basic FastAPI app and CORS middleware

---

## Phase 2: Foundational (Data Ingestion)

**Purpose**: Ingest textbook content into Qdrant so RAG can function. BLOCKS all user stories.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create `backend/app/services/qdrant.py` to handle Qdrant client connection and collection creation
- [x] T007 Create `backend/app/services/openai.py` to handle embedding generation
- [x] T008 Create `backend/app/scripts/ingest.py` script to parse Markdown files from `../physical-ai-book/docs/`, chunk content by headers, generate embeddings, and upload to Qdrant
- [ ] T009 Run `ingest.py` to populate the vector database with initial textbook content (Failed: Check QDRANT_URL in .env)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Ask a General Question (Priority: P1) 🎯 MVP

**Goal**: Allow users to ask general questions and get answers based on the book.

**Independent Test**: Send a POST request to `/chat/message` with a query like "What is ROS2?" and verify the streaming response contains relevant info.

### Implementation for User Story 1

- [x] T010 [P] [US1] Define `ChatRequest` and `ChatResponse` schemas in `backend/app/models/schemas.py`
- [x] T011 [US1] Implement RAG retrieval logic in `backend/app/services/rag.py` (search Qdrant based on query)
- [x] T012 [US1] Implement LLM generation logic in `backend/app/services/openai.py` (streaming response using retrieved context)
- [x] T013 [US1] Create `backend/app/api/chat.py` with `/message` endpoint using Server-Sent Events (SSE)
- [x] T014 [US1] Create `physical-ai-book/src/components/Chatbot/styles.module.css` with basic styling
- [x] T015 [US1] Create `physical-ai-book/src/components/Chatbot/ChatWindow.tsx` (UI for input and message list)
- [x] T016 [US1] Create `physical-ai-book/src/components/Chatbot/index.tsx` (Main component, integration with API)
- [x] T017 [US1] Swizzle Docusaurus `Root` or `Layout` to include `<Chatbot />` globally (e.g., `physical-ai-book/src/theme/Root.js`)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 3 - Ask a Question with Page Context (Priority: P1)

**Goal**: Prioritize content from the current page the user is reading.

**Independent Test**: Navigate to "ROS2 Fundamentals", ask "What are nodes?", and verify response cites the current page.

### Implementation for User Story 3

- [x] T018 [US3] Update `ChatRequest` schema in `backend/app/models/schemas.py` to include `current_page` field (optional)
- [x] T019 [US3] Update `backend/app/services/rag.py` to filter or boost Qdrant search results where `metadata.source_page` matches `current_page`
- [x] T020 [US3] Update `physical-ai-book/src/components/Chatbot/index.tsx` to retrieve `window.location.pathname` and pass it in the API request

**Checkpoint**: At this point, User Stories 1 AND 3 should both work independently

---

## Phase 5: User Story 2 - Ask a Question with Text Selection (Priority: P1)

**Goal**: Allow users to select text and ask questions about it.

**Independent Test**: Select a paragraph, type "Explain this", and verify response focuses on the selection.

### Implementation for User Story 2

- [x] T021 [US2] Update `ChatRequest` schema in `backend/app/models/schemas.py` to include `selected_text` field (optional)
- [x] T022 [US2] Update `backend/app/services/rag.py` to treat `selected_text` as high-priority context (prepend to system prompt or hybrid search)
- [x] T023 [US2] Update `physical-ai-book/src/components/Chatbot/index.tsx` to listen for `selectionchange` events or use `window.getSelection()`
- [x] T024 [US2] Update `physical-ai-book/src/components/Chatbot/ChatWindow.tsx` to display a "Quote selected text" indicator in the input area

**Checkpoint**: All P1 stories are now complete

---

## Phase 6: User Story 4 - View Chat History (Priority: P2)

**Goal**: Persist chat history across sessions.

**Independent Test**: Refresh the page and verify previous messages reappear.

### Implementation for User Story 4

- [x] T025 [P] [US4] Define `ChatSession` and `ChatMessage` SQLAlchemy models in `backend/app/models/db.py`
- [x] T026 [US4] Setup Alembic for migrations in `backend/alembic/` and run initial migration (Replaced with init_db.py)
- [x] T027 [US4] Implement CRUD operations for sessions/messages in `backend/app/services/db_service.py`
- [x] T028 [US4] Update `backend/app/api/chat.py` to save messages to DB during the `/message` flow
- [x] T029 [US4] Add `GET /sessions/{session_id}/history` endpoint to `backend/app/api/chat.py`
- [x] T030 [US4] Update `physical-ai-book/src/components/Chatbot/index.tsx` to generate/store `session_id` in localStorage and fetch history on mount

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T031 [P] Add loading states and error handling in Frontend components
- [x] T032 Verify Docusaurus build with `npm run build`
- [ ] T033 Ensure Qdrant ingestion script is robust (handle updates/re-runs)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup. BLOCKS everything else (no data = no RAG).
- **User Story 1 (P1)**: Depends on Foundational.
- **User Story 3 (P1)**: Depends on US1 (modifies existing RAG logic).
- **User Story 2 (P1)**: Depends on US1 (modifies existing RAG logic).
- **User Story 4 (P2)**: Depends on US1 (needs messages to save).

### Parallel Opportunities

- T003, T004 (Config) can run in parallel.
- T010, T014, T015 (Schema, CSS, UI) can run in parallel once Setup is done.
- US3 and US2 are relatively independent enhancements to US1 and could be parallelized by two devs, though they touch the same files.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Ingestion (Critical)
3. Complete Phase 3: User Story 1 (General Chat)
4. **STOP and VALIDATE**: Can I ask "What is ROS2?" and get an answer?

### Incremental Delivery

1. MVP (US1) -> Deploy
2. Add Context Awareness (US3) -> Deploy
3. Add Selection Support (US2) -> Deploy
4. Add History (US4) -> Deploy
