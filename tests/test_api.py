from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_header():
    response = client.get("/")
    assert response.headers.get("x-visites-version") == "0.1.0"
    assert response.status_code == 200
    assert "visites" in response.json()
