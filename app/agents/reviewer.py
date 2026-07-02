from __future__ import annotations

from app.agents.base import AgentContext, AgentResult, BaseAgent


class ReviewerAgent(BaseAgent):
    name = "ReviewerAgent"
    result_key = "review"

    def run(self, context: AgentContext) -> AgentResult:
        plan = context.artifacts.get("plan", {})
        research = context.artifacts.get("research", {})

        steps = plan.get("steps", [])
        findings = research.get("findings", [])

        lines = [
            "Resumo final da orquestracao:",
            f"- Tarefa original: {context.user_task}",
            "- Plano sugerido:",
        ]

        lines.extend([f"  - {step}" for step in steps])
        lines.append("- Achados simulados:")
        lines.extend([f"  - {item['insight']}" for item in findings])
        lines.append(
            "- Conclusao: o fluxo gerou uma resposta auditavel, modular e pronta para evoluir."
        )
        lines.append(
            "- Observacao: esta demonstracao usa agentes simulados, sem integracao com LLM real."
        )

        final_response = "\n".join(lines)

        return AgentResult(
            summary="Final answer reviewed and assembled for API delivery.",
            data={
                "final_response": final_response,
                "quality_checks": [
                    "Plan reviewed",
                    "Research summarized",
                    "Final response assembled",
                ],
            },
        )
