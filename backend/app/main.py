import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from .database import initialize, list_plans, get_plan
from .models import Plan, EstimateRequest, EstimateResponse
from .engine import estimate_cost

@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize()
    yield

app = FastAPI(title="PlanCompare API", version="1.0.0", description="Insurance plan comparison and cost estimation", lifespan=lifespan)
app.add_middleware(CORSMiddleware,    allow_origins=["http://localhost:5173", os.getenv("FRONTEND_URL", "")], allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/plans", response_model=list[Plan])
def plans(search: str | None = Query(default=None, max_length=80)):
    rows = list_plans()
    if search:
        needle = search.casefold()
        rows = [p for p in rows if needle in p["name"].casefold() or needle in p["carrier"].casefold()]
    return rows

@app.get("/api/plans/{plan_id}", response_model=Plan)
def plan_detail(plan_id: int):
    row = get_plan(plan_id)
    if not row:
        raise HTTPException(status_code=404, detail="Plan not found")
    return row

@app.post("/api/estimate", response_model=EstimateResponse)
def estimate(payload: EstimateRequest):
    row = get_plan(payload.plan_id)
    if not row:
        raise HTTPException(status_code=404, detail="Plan not found")
    try:
        return estimate_cost(Plan.model_validate(row), payload.billed_amount, payload.deductible_used)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
