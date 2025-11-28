<!--
Sync Impact Report:
Version change: None (initial creation) -> 1.0.0
Modified principles: All (newly defined)
Added sections: Feature Implementation Strategy, Agent Persona & Behavior
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Textbook Constitution

## Core Principles

### Prime Directive
Our mission is to win the hackathon by delivering a high-quality, interactive, and "AI-Native" textbook for Physical AI & Humanoid Robotics, bridging the gap between digital brains and physical bodies.

### Tech Stack Adherence
We MUST strictly adhere to the defined tech stack:
*   **Frontend**: Docusaurus for static site generation, deployed to GitHub Pages.
*   **Backend**: FastAPI for API, deployed to Vercel/Railway (implied).
*   **RAG Chatbot**: OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier.
*   **Authentication**: Better-Auth for user signup/signin and content personalization.
*   **AI Development**: Claude Code and OpenAI Agents for AI-driven development and content generation.

### Code Quality
All code MUST be Modular, Clean, and well-Documented. We will prioritize readability, maintainability, and scalability to ensure a robust and high-quality final product.

### AI-Native First
Every feature, from core content delivery to bonus functionalities, MUST leverage AI. This includes the RAG chatbot, dynamic content generation, personalized learning paths, and agent skills.

### Proactive Bonus Implementation
We MUST proactively seek opportunities to implement bonus features (Reusable Intelligence via Agent Skills, Auth & Personalization, Dynamic Content, Translation) and ensure they strongly align with the "Physical AI & Humanoid Robotics" theme.

### Deadline-Driven Development
We will maintain a keen focus on the submission deadline of **Sunday, Nov 30, 2025 at 06:00 PM**, ensuring a polished and demo-ready product. We will prioritize core features first, then bonus features in the specified order.

## Feature Implementation Strategy

*   **Core Deliverables**:
    *   AI/Spec-Driven Book Creation: Write a textbook using Docusaurus and deploy it to GitHub Pages.
    *   Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book, utilizing OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, and Qdrant Cloud Free Tier.
*   **Bonus Features (prioritized)**:
    *   **Bonus 1**: Reusable Intelligence (Agent Skills): Create and use reusable intelligence via Claude Code Subagents and Agent Skills.
    *   **Bonus 2**: Auth & Personalization: Implement Signup and Signin using Better-Auth. At signup, ask users about their software and hardware background to personalize content.
    *   **Bonus 3**: Dynamic Content: Enable logged users to personalize content in chapters by pressing a button at the start of each chapter.
    *   **Bonus 4**: Translation: Enable logged users to translate content into Urdu in chapters by pressing a button at the start of each chapter.

## Agent Persona & Behavior

As the AI assistant (Claude Code), I will:
*   Act as an expert AI Solutions Architect and Hackathon Strategist.
*   Be proactive in suggesting and guiding the implementation of bonus features.
*   Ensure all implementations strongly align with the "Physical AI & Humanoid Robotics" theme and the project's Prime Directive.
*   Prioritize technical accuracy and truthfulness in all guidance and actions.
*   Adhere strictly to all "Claude Code Rules" and "Development Guidelines" as defined in the CLAUDE.md file, including diligent PHR and ADR management.

## Governance

This Project Constitution supersedes all other project documentation and practices. Amendments require a documented rationale, explicit approval from the project lead, and a plan for migration/propagation across dependent artifacts. All pull requests and code reviews MUST verify compliance with these principles. Complexity introduced must always be justified by explicit project requirements or significant performance/scalability benefits. Prompt History Records (PHRs) and Architectural Decision Records (ADR) will be maintained diligently.

**Version**: 1.0.0 | **Ratified**: 2025-11-28 | **Last Amended**: 2025-11-28
