from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    database_url: str


settings = Settings(
    app_name=os.getenv("APP_NAME", "fastapi-agent-demo"),
    app_env=os.getenv("APP_ENV", "development"),
    database_url=os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:postgres@db:5432/app",
    ),
)
