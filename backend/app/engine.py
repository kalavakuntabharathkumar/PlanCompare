from .models import Plan, EstimateResponse

def estimate_cost(plan: Plan, billed_amount: float, deductible_used: float = 0) -> EstimateResponse:
    """Estimate member liability using a simplified deductible + copay + coinsurance model."""
    if billed_amount <= 0:
        raise ValueError("billed_amount must be greater than zero")
    if deductible_used < 0:
        raise ValueError("deductible_used cannot be negative")
    remaining_deductible = max(plan.deductible - deductible_used, 0)
    deductible_applied = min(billed_amount, remaining_deductible)
    covered_after_deductible = max(billed_amount - deductible_applied, 0)
    insurer_rate = plan.coverage_percent / 100
    member_coinsurance = covered_after_deductible * (1 - insurer_rate)
    # Copay is only charged when there is a post-deductible covered service amount.
    copay = min(plan.copay, covered_after_deductible) if covered_after_deductible > 0 else 0
    member_cost = min(billed_amount, deductible_applied + member_coinsurance + copay)
    return EstimateResponse(
        plan_id=plan.id, billed_amount=round(billed_amount, 2),
        deductible_applied=round(deductible_applied, 2),
        covered_after_deductible=round(covered_after_deductible, 2),
        coinsurance_rate=round(1 - insurer_rate, 4), copay=round(copay, 2),
        estimated_member_cost=round(member_cost, 2),
        estimated_plan_payment=round(billed_amount - member_cost, 2),
    )
