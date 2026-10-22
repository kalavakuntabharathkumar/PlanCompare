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


def test_deductible_used_above_plan_limit_is_clamped(plan):
    result=estimate_cost(plan,500,900)
    assert result.deductible_applied == 0
    assert result.estimated_member_cost == 125


@pytest.mark.parametrize('billed,used',[(50,0),(100,0),(250,0),(500,0),(750,0),(1000,100),(1500,250),(2000,500),(3000,750),(5000,1000)])
def test_member_and_plan_payments_reconcile_to_billed_amount(plan,billed,used):
    result=estimate_cost(plan,billed,used)
    assert result.estimated_member_cost + result.estimated_plan_payment == pytest.approx(billed)
    assert 0 <= result.estimated_member_cost <= billed
