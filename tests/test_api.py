import fakeredis
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_root_header(monkeypatch):
    fake_redis = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(main, "r", fake_redis)

    response = client.get("/")

    assert response.status_code == 200
    assert response.headers.get("x-visites-version") == "0.1.0"
    assert response.json() == {"visites": 1}


def test_reset(monkeypatch):
    fake_redis = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(main, "r", fake_redis)

    client.get("/")
    client.get("/")

    response = client.post("/reset")

    assert response.status_code == 200
    assert response.json() == {"visites": 0}

    # Après le reset, le compteur doit repartir à 1.
    response = client.get("/")
    assert response.json() == {"visites": 1}
