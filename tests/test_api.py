from fastapi.testclient import TestClient
from app.main import app
from app import storage
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_storage():
    storage.tasks.clear()
    storage.task_id_counter = 1


def test_create_task():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test task"


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task():
    client.post("/tasks", json={"title": "Initial"})
    response = client.put(
        "/tasks/1",
        json={
            "title": "Updated",
            "completed": True
        }
    )
    print(client.get("/tasks").json())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


def test_delete_task():
    client.post("/tasks", json={"title": "To delete"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
