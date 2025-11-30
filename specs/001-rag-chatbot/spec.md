# Feature Specification: Context-Aware RAG Chatbot for Textbook

**Feature Branch**: `001-rag-chatbot`  
**Created**: 2025-11-30  
**Status**: Draft  
**Input**: User description: "Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book. This chatbot must be able to answer user questions about the book's content, including answering questions based only on text selected by the user. Critically, the chatbot must be context-aware of the user's current chapter/lesson to prioritize and tailor its responses."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a General Question (Priority: P1)

A student reading the textbook wants to understand a concept better. They open the chatbot and ask a general question about the book's content. The chatbot should provide a relevant and accurate answer based on the book's content.

**Why this priority**: This is the core functionality of a RAG chatbot – answering questions from the book.

**Independent Test**: Can be fully tested by opening the chatbot, entering a question, and verifying the response's relevance and accuracy.

**Acceptance Scenarios**:

1.  **Given** a student is on any page of the textbook, **When** they type a question (e.g., "What is ROS2?") into the chatbot and submit, **Then** the chatbot displays a concise, accurate answer derived from the textbook content.
2.  **Given** a student asks a question about a topic not covered in the textbook, **When** they submit the question, **Then** the chatbot indicates that it cannot find relevant information in the book and suggests rephrasing or searching the book directly.

---

### User Story 2 - Ask a Question with Text Selection (Priority: P1)

A student reads a specific paragraph and wants more explanation on that exact text. They select the text and ask the chatbot to explain it. The chatbot should use the selected text as primary context for its explanation.

**Why this priority**: Enhances interactivity and provides highly focused assistance, a key differentiator.

**Independent Test**: Can be fully tested by selecting text on a page, initiating a query about it, and observing the chatbot's response.

**Acceptance Scenarios**:

1.  **Given** a student has selected a paragraph of text on a textbook page, **When** they activate the chatbot and ask "Explain this," **Then** the chatbot provides an explanation specifically related to the selected text, citing its source from the textbook.
2.  **Given** a student has selected text and asks a question relevant to it, **When** the chatbot responds, **Then** the response clearly prioritizes the information from the selected text.

---

### User Story 3 - Ask a Question with Page Context (Priority: P1)

A student is on a specific chapter/lesson page and wants clarification on a general concept relevant to that page, without selecting specific text. They ask a general question. The chatbot should prioritize content from the current page in its response.

**Why this priority**: Provides context-aware assistance, making the chatbot more intuitive and helpful.

**Independent Test**: Can be fully tested by navigating to a specific chapter/lesson, asking a general question related to its topic, and verifying the response's focus on that page's content.

**Acceptance Scenarios**:

1.  **Given** a student is viewing "ROS2 Fundamentals" lesson, **When** they ask the chatbot "What are nodes?", **Then** the chatbot's explanation of nodes primarily uses information and examples from the "ROS2 Fundamentals" lesson.
2.  **Given** a student is viewing "Digital Twin Overview" and asks "What is simulation?", **When** the chatbot responds, **Then** the response emphasizes simulation within the context of digital twins, as described on the current page.

---

### User Story 4 - View Chat History (Priority: P2)

A student wants to revisit previous questions and answers from their current session.

**Why this priority**: Improves user experience by allowing continuity of thought.

**Independent Test**: Can be tested by having multiple interactions with the chatbot and then verifying the history display.

**Acceptance Scenarios**:

1.  **Given** a student has had multiple interactions with the chatbot, **When** they open the chatbot, **Then** a scrollable history of their questions and the chatbot's answers is visible for the current session.

---

### Edge Cases

- What happens when the chatbot cannot find relevant information for a query within the textbook?
- How does the chatbot handle ambiguous or extremely broad questions?
- What is the behavior if text selection includes non-text elements or is very long?
- How does the system handle concurrent queries from multiple users (if session-based history is implemented)?
- What is the response if the current page context is malformed or invalid?

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The chatbot MUST be accessible from any page within the published Docusaurus textbook.
-   **FR-002**: The chatbot MUST accept natural language questions from the user.
-   **FR-003**: The chatbot MUST generate responses based *solely* on the content of the textbook.
-   **FR-004**: The chatbot MUST incorporate text selected by the user on the page as a primary contextual input for its responses.
-   **FR-005**: The chatbot MUST receive the current page/lesson context (e.g., file path, unique ID) from the Docusaurus frontend with each query.
-   **FR-006**: When a current page context is provided, the chatbot MUST prioritize retrieving information from that specific page/lesson to formulate its response, especially for general queries.
-   **FR-007**: The chatbot MUST utilize OpenAI's LLM (via Agents/ChatKit SDKs) for answer generation.
-   **FR-008**: The chatbot MUST use Qdrant Cloud Free Tier for storing and retrieving vectorized textbook content.
-   **FR-009**: The chatbot MUST use Neon Serverless Postgres for storing metadata (e.g., content-to-page mapping) and chat history.
-   **FR-010**: The backend API for the chatbot MUST be built using FastAPI.
-   **FR-011**: The frontend integration of the chatbot into Docusaurus MUST be a React component.
-   **FR-012**: The chatbot MUST provide a clear indication when it cannot find an answer within the textbook's content.
-   **FR-013**: The chatbot MUST display its responses within the integrated UI.

### Key Entities *(include if feature involves data)*

-   **TextbookContent**: Represents a segment of the book (e.g., paragraph, section). Attributes: `text`, `embedding`, `source_page_id`, `chapter`, `section`.
-   **UserQuery**: Represents a question posed by the user. Attributes: `query_text`, `selected_text` (optional), `current_page_id` (optional).
-   **ChatResponse**: Represents the chatbot's generated answer. Attributes: `response_text`, `source_references` (optional).
-   **ChatSession**: Represents a user's ongoing conversation. Attributes: `session_id`, `user_id` (if authentication is implemented), `history` (list of UserQuery and ChatResponse pairs).

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: 90% of user questions related to textbook content receive an accurate and relevant answer from the chatbot.
-   **SC-002**: 95% of responses to questions where text is selected accurately reflect and prioritize the selected text as context.
-   **SC-003**: 90% of responses to general questions, when a page context is provided, primarily derive their answers from the content of that specific page/lesson.
-   **SC-004**: Average response time for chatbot queries is under 3 seconds.
-   **SC-005**: Students report a 20% increase in perceived understanding of concepts after using the chatbot compared to just reading the text.
-   **SC-006**: The chatbot successfully integrates into the Docusaurus interface without impacting overall site performance or load times by more than 10%.