# tests.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ingest_and_ask():
    r = client.post("/ingest")
    assert r.status_code == 200

    r = client.get("/ask?q=How did Apple perform last week?")
    assert r.status_code == 200
    assert "answer" in r.json()
