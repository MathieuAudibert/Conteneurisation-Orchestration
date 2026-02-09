FROM node:18-alpine as frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps
COPY frontend/ .
RUN npm run build

FROM python:3.12-slim

LABEL project_name="Conteneurisation-Orchestration"

RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN groupadd -r orchestration_user && useradd -r -g orchestration_user -m -d /home/orchestration_user orchestration_user

WORKDIR /app
COPY pyproject.toml README.md ./
RUN uv pip install --no-cache-dir --system -e .
RUN uv pip install --no-cache-dir --system -e ".[dev]"

COPY backend ./backend
COPY cfg ./cfg
COPY documentation ./documentation

COPY --from=frontend-build /app/frontend/build /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/sites-available/default
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor /var/log/app
RUN chown -R orchestration_user:orchestration_user /app
RUN chown -R orchestration_user:orchestration_user /var/log/app

EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
