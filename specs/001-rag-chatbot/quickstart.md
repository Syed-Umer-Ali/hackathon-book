# Quickstart: RAG Chatbot Development

## Prerequisites

- Node.js 18+
- Python 3.10+
- Docker (optional, for local DBs if not using Cloud)
- API Keys:
  - `OPENAI_API_KEY`
  - `QDRANT_URL` / `QDRANT_API_KEY`
  - `NEON_DATABASE_URL`

## 1. Backend Setup

```bash
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Running the Server

```bash
uvicorn app.api.main:app --reload --port 8000
```

Swagger UI available at `http://localhost:8000/docs`

## 2. Frontend Setup

The frontend is part of the Docusaurus app.

```bash
cd physical-ai-book
npm install
npm start
```

Chatbot should appear as a floating widget on the site.

## 3. Indexing Content

To ingest the textbook content into Qdrant:

```bash
# From backend directory
python -m app.scripts.index_content --docs-dir ../physical-ai-book/docs
```

## 4. Environment Variables

Create a `.env` file in `backend/`:

```ini
OPENAI_API_KEY=sk-...
QDRANT_URL=...
QDRANT_API_KEY=...
DATABASE_URL=postgresql://...
```
