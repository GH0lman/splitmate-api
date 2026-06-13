import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import check_database_connection

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up FastAPI Lifecycle...")
    try:
        check_database_connection()
        logger.info("Database connection verified.")
    except Exception as e:
        logger.error(f"Database connnection failed: {e}")
        raise
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="A multi-tenant REST API for splitting household expenses.",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )
    
    return app

app = create_app()