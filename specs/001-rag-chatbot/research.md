# Research: Context-Aware RAG Chatbot

**Feature**: `001-rag-chatbot`
**Status**: Research Complete

## Decision: Frontend Integration Method
**Decision**: Build a custom React component (`<Chatbot />`) and add it to `Swizzled` Root or Layout, or simply include it in the `Layout` wrapper.
**Rationale**: Docusaurus allows "swizzling" (wrapping) core components. Wrapping the `Root` or `Layout` component ensures the chatbot is persistent across page navigations (SPA feel) and can easily access the current route context.
**Alternatives considered**: 
- *Embedding in Markdown*: Too manual, requires adding to every page.
- *Separate Page*: Breaks the "context-aware" requirement while reading.

## Decision: Backend API Protocol
**Decision**: REST API with Server-Sent Events (SSE) for streaming responses.
**Rationale**: LLM generation takes time. Streaming text to the client improves perceived latency (per Success Criteria SC-004 < 3s). FastAPI supports SSE easily.
**Alternatives considered**: 
- *WebSockets*: Overkill for simple request-response chat, harder to scale serverless.
- *Standard HTTP*: Too slow for long answers.

## Decision: Context Passing Mechanism
**Decision**: Frontend sends `current_path` (slug) and `selected_text` (if any) with every message request.
**Rationale**: The backend is stateless regarding the user's UI navigation. Explicitly sending context ensures accuracy.
**Implementation**:
- `current_path`: `window.location.pathname` or Docusaurus `useLocation()`.
- `selected_text`: `window.getSelection().toString()`.

## Decision: Text Chunking & Indexing Strategy
**Decision**: Chunk by markdown headers (Section/Lesson level) + overlapping sliding window.
**Rationale**: Textbook content is structured. Preserving section boundaries helps the LLM understand the "lesson" context.
**Storage**: Qdrant. Metadata will include `page_slug`, `header_path`, `chapter`.

## Decision: Database Schema for History
**Decision**: Simple relational schema in Neon.
- `sessions` (id, user_id, created_at)
- `messages` (id, session_id, role [user/ai], content, context_used, timestamp)
**Rationale**: Sufficient for storing history and retrieving it for the "View Chat History" user story.
