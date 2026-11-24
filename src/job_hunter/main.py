
from fastapi import FastAPI

from job_hunter.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description=(
        "AI-powered job discovery and recommendation platform."
    ),
    version="0.1.0",
    debug=settings.debug,
)


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "application": settings.app_name,
        "environment": settings.app_env,
    }


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to Job Hunter API",
        "docs": "/docs",
    }