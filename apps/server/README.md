# Flask Server

Tour de App Flask backend server with MySQL database integration.

## Setup

### Install Dependencies

```bash
pip install uv
uv sync
```

### Environment Variables

Create a `.env` file in the server directory:

```env
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=password
DATABASE_NAME=tda_app
PORT=3000
```

### Start MySQL Database

```bash
uv run python db.py
```

## Development

Run the development server:

```bash
uv run python main.py
```

Run with Gunicorn (production):

```bash
uv run gunicorn -w 4 -b 0.0.0.0:3000 main:app
```

## API Endpoints

### Health Check
- **GET** `/api/` - Returns "OK" if server is running

### Users
- **GET** `/api/users` - Get all users from database

## Docker

Build and run with Docker:

```bash
docker build -t flask-server .
docker run -p 3000:3000 --env-file .env flask-server
```

## Project Structure

```
server/
├── src/
│   ├── db/
│   │   ├── __init__.py      # Database connection pool
│   │   └── init.py          # Database schema initialization
│   ├── routes/
│   │   ├── __init__.py
│   │   └── users.py         # User routes
│   └── app.py               # Flask app factory
├── main.py                  # Entry point
├── db.py                    # MySQL Docker helper
├── pyproject.toml           # Python dependencies
├── Dockerfile               # Docker configuration
└── start.sh                 # Startup script for Docker
```

