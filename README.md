# multi-agent-platform-demo

[Read in Portuguese (Brazil)](README.pt-BR.md)

Public FastAPI project that showcases a simple, professional multi-agent orchestration flow. The application receives a user task, runs it through three specialized agents, logs the full execution path, and stores both tasks and execution records in SQLite.

## Featured API Example

This is the main demo flow recruiters and reviewers should try first.

### `POST /tasks`

```bash
curl -X 'POST' \
  'http://localhost:8000/tasks' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "task": "Criar um plano para lancar uma landing page de produto com foco em conversao"
}'
```

### Example response

`id`, timestamps, and execution payload details may vary between runs.

```json
{
  "id": "992f14b8-2ab4-40a4-a191-2847ee23a74d",
  "task": "Criar um plano para lancar uma landing page de produto com foco em conversao",
  "status": "completed",
  "final_response": "Resumo final da orquestracao:\n- Tarefa original: Criar um plano para lancar uma landing page de produto com foco em conversao\n- Plano sugerido:\n  - Entender o resultado esperado pelo usuario\n  - Organizar subetapas relacionadas a criar, plano, lancar\n  - Definir uma sequencia curta para execucao e validacao\n- Achados simulados:\n  - Insight 1: o passo 'Entender o resultado esperado pelo usuario' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n  - Insight 2: o passo 'Organizar subetapas relacionadas a criar, plano, lancar' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n  - Insight 3: o passo 'Definir uma sequencia curta para execucao e validacao' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n- Conclusao: o fluxo gerou uma resposta auditavel, modular e pronta para evoluir.\n- Observacao: esta demonstracao usa agentes simulados, sem integracao com LLM real.",
  "created_at": "2026-07-02T19:08:03.406127",
  "updated_at": "2026-07-02T19:08:03.422875",
  "executions": [
    {
      "id": 1,
      "sequence": 1,
      "agent_name": "PlannerAgent",
      "status": "completed",
      "input_payload": {
        "task": "Criar um plano para lancar uma landing page de produto com foco em conversao",
        "artifacts": {}
      },
      "output_payload": {
        "summary": "Task decomposed into a concise execution plan.",
        "data": {
          "focus_terms": [
            "criar",
            "plano",
            "lancar"
          ],
          "steps": [
            "Entender o resultado esperado pelo usuario",
            "Organizar subetapas relacionadas a criar, plano, lancar",
            "Definir uma sequencia curta para execucao e validacao"
          ]
        }
      },
      "started_at": "2026-07-02T19:08:03.419636",
      "completed_at": "2026-07-02T19:08:03.419807"
    },
    {
      "id": 2,
      "sequence": 2,
      "agent_name": "ResearchAgent",
      "status": "completed",
      "input_payload": {
        "task": "Criar um plano para lancar uma landing page de produto com foco em conversao",
        "artifacts": {
          "plan": {
            "focus_terms": [
              "criar",
              "plano",
              "lancar"
            ],
            "steps": [
              "Entender o resultado esperado pelo usuario",
              "Organizar subetapas relacionadas a criar, plano, lancar",
              "Definir uma sequencia curta para execucao e validacao"
            ]
          }
        }
      },
      "output_payload": {
        "summary": "Simulated research findings generated for each planning step.",
        "data": {
          "findings": [
            {
              "topic": "Entender o resultado esperado pelo usuario",
              "source_type": "simulated_internal_brief",
              "insight": "Insight 1: o passo 'Entender o resultado esperado pelo usuario' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
              "confidence": 0.78
            },
            {
              "topic": "Organizar subetapas relacionadas a criar, plano, lancar",
              "source_type": "simulated_internal_brief",
              "insight": "Insight 2: o passo 'Organizar subetapas relacionadas a criar, plano, lancar' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
              "confidence": 0.84
            },
            {
              "topic": "Definir uma sequencia curta para execucao e validacao",
              "source_type": "simulated_internal_brief",
              "insight": "Insight 3: o passo 'Definir uma sequencia curta para execucao e validacao' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
              "confidence": 0.9
            }
          ],
          "notes": [
            "Pesquisa simulada para fins de demonstracao.",
            "Nenhum provider externo foi chamado durante a execucao."
          ]
        }
      },
      "started_at": "2026-07-02T19:08:03.419917",
      "completed_at": "2026-07-02T19:08:03.419955"
    },
    {
      "id": 3,
      "sequence": 3,
      "agent_name": "ReviewerAgent",
      "status": "completed",
      "input_payload": {
        "task": "Criar um plano para lancar uma landing page de produto com foco em conversao",
        "artifacts": {
          "plan": {
            "focus_terms": [
              "criar",
              "plano",
              "lancar"
            ],
            "steps": [
              "Entender o resultado esperado pelo usuario",
              "Organizar subetapas relacionadas a criar, plano, lancar",
              "Definir uma sequencia curta para execucao e validacao"
            ]
          },
          "research": {
            "findings": [
              {
                "topic": "Entender o resultado esperado pelo usuario",
                "source_type": "simulated_internal_brief",
                "insight": "Insight 1: o passo 'Entender o resultado esperado pelo usuario' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
                "confidence": 0.78
              },
              {
                "topic": "Organizar subetapas relacionadas a criar, plano, lancar",
                "source_type": "simulated_internal_brief",
                "insight": "Insight 2: o passo 'Organizar subetapas relacionadas a criar, plano, lancar' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
                "confidence": 0.84
              },
              {
                "topic": "Definir uma sequencia curta para execucao e validacao",
                "source_type": "simulated_internal_brief",
                "insight": "Insight 3: o passo 'Definir uma sequencia curta para execucao e validacao' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.",
                "confidence": 0.9
              }
            ],
            "notes": [
              "Pesquisa simulada para fins de demonstracao.",
              "Nenhum provider externo foi chamado durante a execucao."
            ]
          }
        }
      },
      "output_payload": {
        "summary": "Final answer reviewed and assembled for API delivery.",
        "data": {
          "final_response": "Resumo final da orquestracao:\n- Tarefa original: Criar um plano para lancar uma landing page de produto com foco em conversao\n- Plano sugerido:\n  - Entender o resultado esperado pelo usuario\n  - Organizar subetapas relacionadas a criar, plano, lancar\n  - Definir uma sequencia curta para execucao e validacao\n- Achados simulados:\n  - Insight 1: o passo 'Entender o resultado esperado pelo usuario' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n  - Insight 2: o passo 'Organizar subetapas relacionadas a criar, plano, lancar' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n  - Insight 3: o passo 'Definir uma sequencia curta para execucao e validacao' tende a ganhar qualidade quando possui criterio de sucesso explicito e contexto minimo.\n- Conclusao: o fluxo gerou uma resposta auditavel, modular e pronta para evoluir.\n- Observacao: esta demonstracao usa agentes simulados, sem integracao com LLM real.",
          "quality_checks": [
            "Plan reviewed",
            "Research summarized",
            "Final response assembled"
          ]
        }
      },
      "started_at": "2026-07-02T19:08:03.419995",
      "completed_at": "2026-07-02T19:08:03.420032"
    }
  ]
}
```

## What this project does

`multi-agent-platform-demo` exposes a simple API that accepts a task, processes it through three agents, saves execution traces, and returns a final structured answer.

Core capabilities:

- `POST /tasks` receives and processes a task
- `GET /tasks/{id}` returns the persisted result and execution history
- Every agent step stores input, output, status, timestamps, and execution order
- The architecture is intentionally simple and ready for new agents

## What agents are

In this project, an agent is a focused component responsible for one part of a larger workflow.

- `PlannerAgent`: breaks the incoming task into actionable steps
- `ResearchAgent`: produces simulated findings for each planned step
- `ReviewerAgent`: reviews previous outputs and assembles the final answer

This separation makes the demo easier to understand, test, extend, and discuss in interviews.

## Agent flow

```mermaid
flowchart LR
    A["User submits task"] --> B["POST /tasks"]
    B --> C["TaskService creates Task"]
    C --> D["PlannerAgent"]
    D --> E["ResearchAgent"]
    E --> F["ReviewerAgent"]
    F --> G["SQLite stores task and execution logs"]
    G --> H["API returns final response"]
    H --> I["GET /tasks/{id} fetches history"]
```

## Architecture

```text
app/
|- agents/        # Base interface and concrete agents
|- api/           # FastAPI routes
|- services/      # Orchestration and business logic
|- db.py          # Engine, session, and database bootstrap
|- models.py      # SQLAlchemy models
|- schemas.py     # Pydantic schemas
|- main.py        # Application entry point
```

## Tech stack

- Python 3.12
- FastAPI
- SQLite
- SQLAlchemy 2.x
- Pydantic 2.x
- Pytest
- Docker
- GitHub Actions

## Installation and local run

### Local environment

```bash
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install ".[dev]"
uvicorn app.main:app --reload
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install ".[dev]"
uvicorn app.main:app --reload
```

Available at:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

### Docker

```bash
docker compose up --build
```

## More curl examples

### Get a stored task

```bash
curl "http://127.0.0.1:8000/tasks/<TASK_ID>"
```

## Challenges and solutions

### 1. Demonstrating agents without coupling the demo to a real LLM

Solution:
The agents are deterministic and simulated by default. That keeps the project lightweight, testable, and ready for a future provider integration.

### 2. Keeping the code simple without losing extensibility

Solution:
A shared `BaseAgent` interface and a separate orchestration layer keep the HTTP layer small and make new agents easy to add.

### 3. Making the workflow observable

Solution:
Each execution step persists `input_payload`, `output_payload`, timestamps, status, and sequence so the run can be inspected end to end.

## Future improvements

- Add asynchronous execution with a queue
- Integrate a real LLM through a configurable provider layer
- Expose streaming execution events
- Add authentication and user ownership
- Build a small dashboard for task history
- Publish a real deployment on Railway, Render, or Fly.io

## Author

Gabriel Quintino

- LinkedIn: [https://www.linkedin.com/in/seu-linkedin](https://www.linkedin.com/in/seu-linkedin)
- Email: [gabriel.quintino@exemplo.com](mailto:gabriel.quintino@exemplo.com)
