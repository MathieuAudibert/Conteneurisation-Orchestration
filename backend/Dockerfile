FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

LABEL project_name="Conteneurisation-Orchestration"

RUN groupadd -r orchestration_user && useradd -r -g orchestration_user -m -d /home/orchestration_user orchestration_user

WORKDIR /app
COPY pyproject.toml ./

RUN uv pip install --no-cache-dir --system -e .

COPY . .
RUN chown -R orchestration_user:orchestration_user /app
USER orchestration_user

CMD ["fastapi", "dev", "backend/src/main.py", "--host", "0.0.0.0"]