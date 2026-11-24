
# AI Job Finder

An AI-powered job discovery and recommendation platform.

AI Job Finder analyzes professional profiles, searches multiple job sources,
and recommends opportunities using semantic matching and LLM-powered reasoning.

## Features

- CV parsing and professional profile extraction.
- Natural language job search.
- Multi-source job aggregation.
- Semantic matching using embeddings.
- AI-powered job recommendations.
- Conversational assistant.
- Job tracking and favorites.

## Architecture

The project follows a modular architecture:

- API: FastAPI
- Frontend: Streamlit
- AI: LLMs and Sentence Transformers
- Database: PostgreSQL and pgvector
- Testing: Pytest
- Infrastructure: Docker

## Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/ai-job-finder.git

cd ai-job-finder

### 2. Create virtual environment

python -m venv .venv

### 3. Install dependencies

pip install -e ".[dev]"

### 4. Configure environment

cp .env.example .env

### 5. Run the API

uvicorn ai_job_finder.main:app --reload --app-dir src

## Testing

pytest

## API Documentation

http://127.0.0.1:8000/docs