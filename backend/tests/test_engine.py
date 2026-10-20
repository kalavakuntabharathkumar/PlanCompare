import pytest
from app.engine import estimate_cost
from app.models import Plan

@pytest.fixture
def plan():
    return Plan(id=1,name="Test",carrier="Carrier",annual_premium=1000,deductible=500,copay=25,coverage_percent=80)

def test_deductible_and_coinsurance_are_applied_in_order(plan):
    result=estimate_cost(plan,1000,0)
    assert result.deductible_applied == 500
    assert result.covered_after_deductible == 500
    assert result.estimated_member_cost == 625
    assert result.estimated_plan_payment == 375

def test_existing_deductible_spend_reduces_member_cost(plan):
    result=estimate_cost(plan,1000,500)
    assert result.deductible_applied == 0
    assert result.estimated_member_cost == 225

def test_small_claim_is_capped_at_billed_amount(plan):
    result=estimate_cost(plan,100,0)
    assert result.estimated_member_cost == 100
    assert result.estimated_plan_payment == 0

def test_invalid_billed_amount_rejected(plan):
    with pytest.raises(ValueError): estimate_cost(plan,0)

def test_negative_deductible_spend_rejected(plan):
    with pytest.raises(ValueError): estimate_cost(plan,100,-1)
