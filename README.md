# AI News Analyst Agent

A multi-agent system that ingests news from multiple sources, processes and stores it using a RAG architecture, and uses specialized LLM agents to extract entities, analyze bias/sentiment, compare contradictory reports, and generate rich insights based on real-world impact.

## Architecture
- **FastAPI** for core API routing and async jobs.
- **MongoDB** for document store (raw articles, processed texts, reports).
- **ChromaDB** for RAG vector embeddings.
- **LiteLLM / OpenAI** for dynamic LLM agent routing.
- **Spacy / newspaper3k** for local entity extraction and scraping.

## Quickstart
1. Clone the repository.
2. Form your `.env` file based on `.env.example`.
3. Boot the environment utilizing Docker:
   ```bash
   docker-compose up --build
   ```
4. Find the auto-generated Swagger documentation at `http://localhost:8000/docs`.
