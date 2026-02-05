FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

LABEL project_name="Conteneurisation-Orchestration"

WORKDIR /app

COPY pyproject.toml README.md ./
COPY documentation ./documentation
COPY cfg ./cfg

RUN uv pip install --no-cache-dir --system -e ".[dev]"

WORKDIR /app/documentation

CMD ["zensical", "serve", "-a", "0.0.0.0:7777"]
