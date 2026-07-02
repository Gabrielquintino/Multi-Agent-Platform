from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentContext:
    task_id: str
    user_task: str
    artifacts: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentResult:
    summary: str
    data: dict[str, Any]


class BaseAgent(ABC):
    name: str
    result_key: str

    @abstractmethod
    def run(self, context: AgentContext) -> AgentResult:
        """Execute the agent and return structured output."""
