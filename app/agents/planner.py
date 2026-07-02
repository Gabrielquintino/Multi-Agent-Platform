from __future__ import annotations

import re

from app.agents.base import AgentContext, AgentResult, BaseAgent


class PlannerAgent(BaseAgent):
    name = "PlannerAgent"
    result_key = "plan"

    def run(self, context: AgentContext) -> AgentResult:
        keywords = self._extract_keywords(context.user_task)
        focus = ", ".join(keywords) if keywords else "objetivo principal"
        steps = [
            "Entender o resultado esperado pelo usuario",
            f"Organizar subetapas relacionadas a {focus}",
            "Definir uma sequencia curta para execucao e validacao",
        ]

        return AgentResult(
            summary="Task decomposed into a concise execution plan.",
            data={
                "focus_terms": keywords,
                "steps": steps,
            },
        )

    def _extract_keywords(self, task: str) -> list[str]:
        words = re.findall(r"[A-Za-z0-9]+", task.lower())
        stop_words = {
            "para",
            "com",
            "uma",
            "de",
            "que",
            "como",
            "sobre",
            "das",
            "dos",
            "por",
            "the",
            "and",
            "with",
            "this",
        }
        filtered = [word for word in words if len(word) > 3 and word not in stop_words]

        unique_words: list[str] = []
        for word in filtered:
            if word not in unique_words:
                unique_words.append(word)

        return unique_words[:3]
