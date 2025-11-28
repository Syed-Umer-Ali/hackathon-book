---
id: 0001
title: Initial Project Constitution
stage: constitution
date: 2025-11-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Act as an expert AI Solutions Architect and Hackathon Strategist. I am participating in a high-stakes hackathon to build a "Physical AI & Humanoid Robotics" textbook and learning platform.

I need you to write a comprehensive "Project Constitution" (System Prompt / Master Plan) that will govern our development process and the behavior of the AI agents we build.

Here are the full project requirements and context:

<PROJECT_CONTEXT>
 'Hackathon_ Physical AI & Humanoid Robotics Textbook.md' here]
</PROJECT_CONTEXT>

Based on the above context, generate a **Project Constitution** that includes the following sections:

1.  **Prime Directive**: A clear mission statement focused on winning the hackathon by delivering a high-quality, interactive, and "AI-Native" textbook.
2.  **Tech Stack & Architecture**: A strict definition of the technologies we MUST use (Docusaurus, Spec-Kit Plus, Claude Code, OpenAI Agents, FastAPI, Neon Postgres, Qdrant, Better-Auth). Define how these components interact.
3.  **Development Rules**:
    *   Code Quality Standards (Modular, Clean, Documented).
    *   "AI-Native" First: Every feature must leverage AI (e.g., the RAG chatbot, dynamic content).
    *   Deployment Strategy: GitHub Pages for frontend, Vercel/Railway for backend (implied).
4.  **Feature Implementation Strategy**:
    *   **Core**: Book content + RAG Chatbot.
    *   **Bonus 1**: Reusable Intelligence (Agent Skills).
    *   **Bonus 2**: Auth & Personalization (Better-Auth).
    *   **Bonus 3 & 4**: Dynamic Content & Translation.
5.  **Agent Persona & Behavior**: Define how YOU (the AI assistant helping me) should behave. You should be proactive, suggest "Bonus" implementations eagerly, and ensure we hit the "Physical AI" theme hard.
6.  **Timeline Management**: A strategy to ensure we hit the Nov 30th deadline with a polished demo.

The output should be a structured Markdown document that I can use as a "System Prompt" for my coding sessions or as a "Readme" for the team.
command: /sp.constitution
labels: ["constitution", "project-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

Act as an expert AI Solutions Architect and Hackathon Strategist. I am participating in a high-stakes hackathon to build a "Physical AI & Humanoid Robotics" textbook and learning platform.

I need you to write a comprehensive "Project Constitution" (System Prompt / Master Plan) that will govern our development process and the behavior of the AI agents we build.

Here are the full project requirements and context:

<PROJECT_CONTEXT>
 'Hackathon_ Physical AI & Humanoid Robotics Textbook.md' here]
</PROJECT_CONTEXT>

Based on the above context, generate a **Project Constitution** that includes the following sections:

1.  **Prime Directive**: A clear mission statement focused on winning the hackathon by delivering a high-quality, interactive, and "AI-Native" textbook.
2.  **Tech Stack & Architecture**: A strict definition of the technologies we MUST use (Docusaurus, Spec-Kit Plus, Claude Code, OpenAI Agents, FastAPI, Neon Postgres, Qdrant, Better-Auth). Define how these components interact.
3.  **Development Rules**:
    *   Code Quality Standards (Modular, Clean, Documented).
    *   "AI-Native" First: Every feature must leverage AI (e.g., the RAG chatbot, dynamic content).
    *   Deployment Strategy: GitHub Pages for frontend, Vercel/Railway for backend (implied).
4.  **Feature Implementation Strategy**:
    *   **Core**: Book content + RAG Chatbot.
    *   **Bonus 1**: Reusable Intelligence (Agent Skills).
    *   **Bonus 2**: Auth & Personalization (Better-Auth).
    *   **Bonus 3 & 4**: Dynamic Content & Translation.
5.  **Agent Persona & Behavior**: Define how YOU (the AI assistant helping me) should behave. You should be proactive, suggest "Bonus" implementations eagerly, and ensure we hit the "Physical AI" theme hard.
6.  **Timeline Management**: A strategy to ensure we hit the Nov 30th deadline with a polished demo.

The output should be a structured Markdown document that I can use as a "System Prompt" for my coding sessions or as a "Readme" for the team.

## Response snapshot

The Project Constitution has been created and saved to `.specify/memory/constitution.md` (Version 1.0.0).

This initial version defines:
*   The Prime Directive for the hackathon.
*   The strict Tech Stack to be used.
*   Key Development Rules, including Code Quality and "AI-Native" First principles.
*   The Feature Implementation Strategy, prioritizing core and bonus deliverables.
*   The Agent Persona and expected behavior.
*   Project Governance rules.

**Version:** 1.0.0
**Bump Rationale:** This is the initial version of the Project Constitution, establishing the foundational guidelines for the project.

**Files Flagged for Manual Follow-up:**
Please review the following template files to ensure their alignment with the new Project Constitution:
*   `.specify/templates/plan-template.md`
*   `.specify/templates/spec-template.md`
*   `.specify/templates/tasks-template.md`
*   `.specify/templates/commands/*.md`

**Suggested Commit Message:**
```
docs: initial project constitution v1.0.0 (prime directive, tech stack, dev rules, feature strategy, agent persona, governance)
```

## Outcome

- ✅ Impact: The project constitution has been successfully created, defining core principles, tech stack, development rules, feature strategy, agent persona, and governance rules.
- 🧪 Tests: N/A
- 📁 Files: One file created/modified: .specify/memory/constitution.md
- 🔁 Next prompts: Review of template alignment, then feature specification.
- 🧠 Reflection: Successfully created the initial project constitution, incorporating all user requirements and adhering to the specified format. Ensured all placeholders were correctly filled. Identified template files that require manual follow-up for alignment.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: Ensure smooth propagation of constitutional changes to dependent templates (spec, plan, tasks, commands) during future development.
