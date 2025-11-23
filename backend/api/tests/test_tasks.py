import pytest
from fastapi.testclient import TestClient
from config.asgi import app

client = TestClient(app)

def test_read_root():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}

@pytest.mark.django_db(transaction=True) # transaction=True might be needed for sync_to_async/thread compatibility
def test_create_and_list_tasks():
    # List tasks - empty
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert response.json() == []

    # Create task
    task_data = {
        "title": "Integration Test Task",
        "priority": 3,
        "description": "Testing hybrid architecture"
    }
    response = client.post("/api/v1/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Integration Test Task"
    assert data["id"] is not None

    # List tasks - should have 1
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1
