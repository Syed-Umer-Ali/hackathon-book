# Implementation Plan: Context-Aware RAG Chatbot

**Branch**: `001-rag-chatbot` | **Date**: 2025-11-30 | **Spec**: [specs/001-rag-chatbot/spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a Retrieval-Augmented Generation (RAG) chatbot embedded in the Docusaurus textbook. The chatbot will use OpenAI for generation, Qdrant for vector storage of book content, and Neon Postgres for chat history. It will feature context awareness (current page) and text selection support.

## Technical Context

**Language/Version**: Python 3.10+ (Backend), TypeScript 5+ (Frontend)
**Primary Dependencies**: 
- Backend: FastAPI, OpenAI SDK, Qdrant Client, SQLAlchemy/AsyncPG
- Frontend: React 18, Docusaurus Core
**Storage**: Neon Serverless Postgres (History/Metadata), Qdrant Cloud (Vector)
**Testing**: pytest (Backend), Jest (Frontend)
**Target Platform**: 
- Frontend: Static Web (GitHub Pages)
- Backend: Cloud Container/Serverless (Hosting TBD - e.g., Render/Railway)
**Project Type**: Web application (Full stack: Static Frontend + API Backend)
**Performance Goals**: Response < 3s
**Constraints**: Free Tier usage for Qdrant/Neon.
**Scale/Scope**: Single textbook, potentially hundreds of students.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. AI/Spec-Driven Development**: Plan follows SDD.
- **II. Docusaurus-First**: Chatbot integrated into Docusaurus.
- **III. Context-Aware RAG Chatbot**: Core feature being built.
- **VI. Robust Technology Stack**: Matches specified stack (OpenAI, FastAPI, Neon, Qdrant).

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
backend/                 # New Python Backend
├── app/
│   ├── api/             # Endpoints
│   ├── core/            # Config, Security
│   ├── db/              # Database connection
│   ├── models/          # Pydantic/SQLAlchemy models
│   └── services/        # RAG logic, OpenAI, Qdrant
├── tests/
└── requirements.txt

physical-ai-book/        # Existing Docusaurus
├── src/
│   ├── components/
│   │   └── Chatbot/     # New React Component
│   │       ├── index.tsx
│   │       ├── ChatWindow.tsx
│   │       └── styles.module.css
│   └── ...
└── ...
```

**Structure Decision**: Split structure. Frontend code resides within the existing `physical-ai-book` Docusaurus project. Backend code resides in a new root-level `backend/` directory to keep concerns separated and deployable independently.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | | |
