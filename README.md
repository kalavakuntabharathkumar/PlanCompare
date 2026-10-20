# PlanCompare

An employee-facing insurance plan comparison app with an auditable out-of-pocket estimator. The Vue 3 client compares plans; a FastAPI service calculates member cost from deductible, co-pay, and coverage rules.

## Stack
Vue 3 · TypeScript · Pinia · Vite · Vitest · Python · FastAPI · Pydantic · SQLite · pytest

## Start

Backend:
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate | macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Frontend (second terminal):
```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL (normally `http://localhost:5173`). API docs are at `http://localhost:8000/docs`.

## Cost model
The estimate applies the remaining deductible first, then calculates the member's coinsurance on the covered amount, adds the fixed co-pay, and caps the member amount at the billed amount. This is a simplified educational estimator; real policies may include out-of-pocket maximums, exclusions, networks, service-specific rules, and family deductibles.

## Tests
```bash
cd backend && pytest
cd frontend && npm test
```
