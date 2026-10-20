from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health():
    assert client.get('/health').json()=={'status':'ok'}

def test_plans_returns_seeded_catalog():
    response=client.get('/api/plans')
    assert response.status_code==200
    assert len(response.json())>=4

def test_search_filters_plans():
    response=client.get('/api/plans',params={'search':'Cedar'})
    assert response.status_code==200
    assert all('Cedar' in p['carrier'] for p in response.json())

def test_estimate_endpoint():
    response=client.post('/api/estimate',json={'plan_id':1,'billed_amount':1000,'deductible_used':0})
    assert response.status_code==200
    assert response.json()['estimated_member_cost']==625

def test_unknown_plan_returns_404():
    assert client.post('/api/estimate',json={'plan_id':999,'billed_amount':100}).status_code==404
