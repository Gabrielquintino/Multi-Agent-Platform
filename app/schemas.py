from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):
    task: str = Field(..., min_length=3, max_length=4000, description="Task provided by the user.")


class TaskExecutionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sequence: int
    agent_name: str
    status: str
    input_payload: dict[str, Any]
    output_payload: dict[str, Any]
    started_at: datetime
    completed_at: datetime


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    task: str
    status: str
    final_response: str | None
    created_at: datetime
    updated_at: datetime
    executions: list[TaskExecutionRead]
