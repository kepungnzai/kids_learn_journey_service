# Kids Learn Journey

This repository contains the Kids Courses GraphQL API using FastAPI, Strawberry, and MongoDB.

## Startup Instructions

1. Change into the API project directory:
   ```bash
   cd kids-courses-api
   ```

2. Install dependencies with `uv`:
   ```bash
   uv sync
   ```

3. Start the server:
   ```bash
   uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```

4. Open GraphQL at:
   ```text
   http://127.0.0.1:8000/graphql
   ```

## Notes

- The project uses `uv` as the package manager and runtime launcher.
- The API exposes GraphQL queries and mutations for courses and user accounts.
