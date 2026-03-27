from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_docs():
    """Verify the API documentation endpoint is alive (booting success)."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_app_configuration():
    """Verify the app loads with the expected configuration and namespaces."""
    assert app.title == "AI News Analyst"
    assert app.version == "1.0.0"
