from __future__ import annotations

from copy import deepcopy

from app.agents import AgentContext, BaseAgent, PlannerAgent, ResearchAgent, ReviewerAgent
from app.models import Task, TaskExecution, utcnow


class TaskOrchestrator:
    def __init__(self, agents: list[BaseAgent]):
        self.agents = agents

    def run(self, session, task: Task) -> Task:
        task.status = "running"
        context = AgentContext(task_id=task.id, user_task=task.task)
        last_sequence = 0

        try:
            for sequence, agent in enumerate(self.agents, start=1):
                last_sequence = sequence
                started_at = utcnow()
                input_payload = {
                    "task": context.user_task,
                    "artifacts": deepcopy(context.artifacts),
                }

                result = agent.run(context)
                context.artifacts[agent.result_key] = result.data

                execution = TaskExecution(
                    task_id=task.id,
                    sequence=sequence,
                    agent_name=agent.name,
                    status="completed",
                    input_payload=input_payload,
                    output_payload={
                        "summary": result.summary,
                        "data": result.data,
                    },
                    started_at=started_at,
                    completed_at=utcnow(),
                )
                session.add(execution)

            task.final_response = context.artifacts["review"]["final_response"]
            task.status = "completed"
            session.commit()
            session.refresh(task)
            return task
        except Exception as exc:
            failure_log = TaskExecution(
                task_id=task.id,
                sequence=last_sequence or 1,
                agent_name=self.agents[last_sequence - 1].name if last_sequence else "orchestrator",
                status="failed",
                input_payload={"task": context.user_task, "artifacts": deepcopy(context.artifacts)},
                output_payload={"error": str(exc)},
                started_at=utcnow(),
                completed_at=utcnow(),
            )
            session.add(failure_log)
            task.status = "failed"
            task.final_response = "Task orchestration failed."
            session.commit()
            raise


def build_default_orchestrator() -> TaskOrchestrator:
    return TaskOrchestrator(
        agents=[
            PlannerAgent(),
            ResearchAgent(),
            ReviewerAgent(),
        ]
    )
