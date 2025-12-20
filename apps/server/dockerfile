FROM python:3.13-alpine

RUN apk add --no-cache bash netcat-openbsd

WORKDIR /app

COPY pyproject.toml ./

RUN pip install uv && uv sync

COPY . .

RUN chmod +x /app/start.sh


ENV PORT=3000

EXPOSE 3000

CMD ["/app/start.sh"]

