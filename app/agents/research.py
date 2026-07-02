from __future__ import annotations

from app.agents.base import AgentContext, AgentResult, BaseAgent


class ResearchAgent(BaseAgent):
    name = "ResearchAgent"
    result_key = "research"

    def run(self, context: AgentContext) -> AgentResult:
        plan = context.artifacts.get("plan", {})
        steps = plan.get("steps", [])

        findings = []
        for index, step in enumerate(steps, start=1):
            findings.append(
                {
                    "topic": step,
                    "source_type": "simulated_internal_brief",
                    "insight": (
                        f"Insight {index}: o passo '{step}' tende a ganhar qualidade "
                        "quando possui criterio de sucesso explicito e contexto minimo."
                    ),
                    "confidence": round(0.72 + (index * 0.06), 2),
                }
            )

        return AgentResult(
            summary="Simulated research findings generated for each planning step.",
            data={
                "findings": findings,
                "notes": [
                    "Pesquisa simulada para fins de demonstracao.",
                    "Nenhum provider externo foi chamado durante a execucao.",
                ],
            },
        )
