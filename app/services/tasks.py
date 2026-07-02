from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import Task
from app.schemas import TaskCreate
from app.services.orchestrator import build_default_orchestrator


class TaskService:
    def __init__(self, session: Session):
        self.session = session
        self.orchestrator = build_default_orchestrator()

    def create_task(self, payload: TaskCreate) -> Task:
        task = Task(task=payload.task, status="pending")
        self.session.add(task)
        self.session.flush()

        self.orchestrator.run(self.session, task)
        return self.get_task(task.id)  # type: ignore[return-value]

    def get_task(self, task_id: str) -> Task | None:
        statement = (
            select(Task)
            .options(selectinload(Task.executions))
            .where(Task.id == task_id)
        )
        return self.session.execute(statement).scalar_one_or_none()
