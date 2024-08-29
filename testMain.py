from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate():
    response = client.post("/generate", json={"texto": "hola"})
    assert response.status_code == 200
    assert response.json() == {"checksum": 421}

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido, [Nombre del Participante]!"}
