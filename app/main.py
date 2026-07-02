from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.tasks import router as tasks_router
from app.db import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="multi-agent-platform-demo",
    description="Simple FastAPI demo for multi-agent orchestration.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(tasks_router)


@app.get("/", tags=["meta"])
def read_root() -> dict[str, str]:
    return {
        "name": "multi-agent-platform-demo",
        "status": "ok",
        "docs": "/docs",
    }
