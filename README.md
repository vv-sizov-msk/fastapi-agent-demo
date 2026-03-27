# fastapi-agent-demo

Небольшой production-style шаблон сервиса на FastAPI с PostgreSQL, SQLAlchemy 2.x, Alembic, pytest, Docker Compose и CI в GitHub Actions.

## Стек

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x
- Alembic
- pytest
- Docker Compose
- GitHub Actions

## Структура

```text
.
├── app/
│   ├── api/
│   │   └── health.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── item.py
│   └── main.py
├── alembic/
│   └── versions/
├── tests/
│   └── test_health.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Запуск локально

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Проверка healthcheck:

```bash
curl http://localhost:8000/health
```

## Запуск через Docker Compose

```bash
docker compose up --build
```

## Миграции

Создать новую миграцию:

```bash
alembic revision --autogenerate -m "message"
```

Применить миграции:

```bash
alembic upgrade head
```

## Тесты

```bash
pytest
```
