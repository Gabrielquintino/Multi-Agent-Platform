from __future__ import annotations

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db import Base, get_session
from app.main import app


@pytest.fixture()
def client(tmp_path) -> Generator[TestClient, None, None]:
    database_path = tmp_path / "test.db"
    engine = create_engine(
        f"sqlite:///{database_path}",
        connect_args={"check_same_thread": False},
    )
    testing_session_local = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )

    Base.metadata.create_all(bind=engine)

    def override_get_session() -> Generator[Session, None, None]:
        session = testing_session_local()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_create_task_runs_three_agents_and_persists_logs(client: TestClient) -> None:
    response = client.post(
        "/tasks",
        json={
            "task": "Criar um plano de onboarding para novos colaboradores da plataforma",
        },
    )

    assert response.status_code == 201

    payload = response.json()
    assert payload["status"] == "completed"
    assert payload["task"].startswith("Criar um plano")
    assert len(payload["executions"]) == 3
    assert [item["agent_name"] for item in payload["executions"]] == [
        "PlannerAgent",
        "ResearchAgent",
        "ReviewerAgent",
    ]
    assert "agentes simulados" in payload["final_response"]


def test_get_task_returns_existing_record(client: TestClient) -> None:
    create_response = client.post(
        "/tasks",
        json={"task": "Organizar uma estrategia para demo tecnica com multiplos agentes"},
    )
    task_id = create_response.json()["id"]

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 200
    payload = get_response.json()
    assert payload["id"] == task_id
    assert payload["status"] == "completed"
    assert payload["executions"][0]["sequence"] == 1


def test_get_task_returns_404_for_unknown_id(client: TestClient) -> None:
    response = client.get("/tasks/not-found")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
