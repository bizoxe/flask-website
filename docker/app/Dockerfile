FROM python:3.12.6-bookworm

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv

RUN uv pip install --system -r pyproject.toml

COPY src/ ./src/
COPY app.py gunicorn.conf.py ./

EXPOSE 8000

CMD ["gunicorn", "app:app"]
