from pydantic import BaseModel, Field, ConfigDict

class Plan(BaseModel):
    id: int
    name: str
    carrier: str
    annual_premium: float = Field(ge=0)
    deductible: float = Field(ge=0)
    copay: float = Field(ge=0)
    coverage_percent: float = Field(ge=0, le=100)
    model_config = ConfigDict(from_attributes=True)

class EstimateRequest(BaseModel):
    plan_id: int
    billed_amount: float = Field(gt=0, le=1_000_000)
    deductible_used: float = Field(default=0, ge=0)

class EstimateResponse(BaseModel):
    plan_id: int
    billed_amount: float
    deductible_applied: float
    covered_after_deductible: float
    coinsurance_rate: float
    copay: float
    estimated_member_cost: float
    estimated_plan_payment: float
