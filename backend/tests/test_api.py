import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_health(client):
    assert client.get('/health').json()=={'status':'ok'}

def test_plans_returns_seeded_catalog(client):
    response=client.get('/api/plans')
    assert response.status_code==200
    assert len(response.json())>=4

def test_search_filters_plans(client):
    response=client.get('/api/plans',params={'search':'Cedar'})
    assert response.status_code==200
    assert all('Cedar' in p['carrier'] for p in response.json())

def test_estimate_endpoint(client):
    response=client.post('/api/estimate',json={'plan_id':3,'billed_amount':1000,'deductible_used':0})
    assert response.status_code==200
    assert response.json()['estimated_member_cost']==340

def test_unknown_plan_returns_404(client):
    assert client.post('/api/estimate',json={'plan_id':999,'billed_amount':100}).status_code==404
