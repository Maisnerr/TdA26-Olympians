#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."

until nc -z ${DATABASE_HOST:-localhost} ${DATABASE_PORT:-3306}; do
  echo "MySQL is unavailable - sleeping"
  sleep 2
done

echo "MySQL is up - starting server"
uv run gunicorn -w 4 -b 0.0.0.0:${PORT:-3000} main:app

