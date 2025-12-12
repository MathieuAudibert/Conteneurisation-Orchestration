FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN groupadd -r orchestration_user && useradd -r -g esilv -m -d /home/orchestration_user orchestration_user

WORKDIR /app
COPY pyproject.toml requirements.txt ./

RUN uv pip install --system -r requirements.txt

COPY . .
RUN chown -R orchestration_user:orchestration_user /app
USER orchestration_user

# TODO: a changer cette commande
CMD ["python", "backend/src/main.py"]