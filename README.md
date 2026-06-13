# Splitmate API

> A multi-tenant REST API for household expense splitting.

## Overview
A flat-mate expense splitting Multi-Tenant REST API project where users can setup household groups that calculates the split of expenses between the members of the specific household. The main focus is on making sure household data is separate and cannot interact by one another.

## Tech Stack
[FastAPI, PostgreSQL, JWT auth, etc.]

## Architecture
[Link to Document](docs/schema-layout.md)

## Getting Started
### Prerequisites
- Python 3.13+
- Docker (for local PostgreSQL 18+)
- Git
### Installation
1. Clone the repository
```bash
   git clone https://github.com/gh0lman/splitmate-api.git
   cd splitmate-api
```

2. Create and activate a virtual environment
```bash
   python -m venv venv
   source venv/bin/activate  # Git Bash / Mac / Linux
   venv\Scripts\Activate.ps1  # Windows PowerShell
```

3. Install dependencies
```bash
   pip install -r requirements-dev.txt
```

4. Start the local database
```bash
   docker run --name splitmate-db \
     -e POSTGRES_USER=myuser \
     -e POSTGRES_PASSWORD=mypassword \
     -e POSTGRES_DB=splitmate \
     -p 5432:5432 \
     -d postgres:18
```

5. Copy the example environment file and fill in your values
```bash
   cp .env.example .env
```

6. Run the development server
```bash
   uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`  
Swagger UI at `http://localhost:8000/docs`

### Environment Variables
Copy `.env.example` to `.env` and configure the following:

| Variable | Description | Example |
|----------|-------------|---------|
| `APP_NAME` | Application name | `Splitmate API` |
| `ENVIRONMENT` | Runtime environment | `development` |
| `DEBUG` | Enable debug mode and SQL logging | `true` |
| `SECRET_KEY` | Secret key for token signing | `change-this-in-production` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:postgres@localhost:5432/splitmate` |
| `BACKEND_CORS_ORIGINS` | Allowed CORS origins as JSON array | `["http://localhost:3000"]` |
| `JWT_ALGORITHM` | Algorithm used for JWT signing | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token lifetime | `30` |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Refresh token lifetime | `7` |
| `LOG_LEVEL` | Logging verbosity | `DEBUG` |

Never commit `.env` file. Always have it listed in `.gitignore`.

## API Documentation
[Link to live Swagger UI once deployed]

## Running Tests

## Deployment

## Design Decisions
[Link to Document](docs/architectural-database-decisions.md)