from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("=" * 60)
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Environment : {settings.ENVIRONMENT}")
    logger.info(f"Version     : {settings.APP_VERSION}")
    logger.info("=" * 60)

    # Startup tasks go here

    yield

    # Shutdown tasks go here
    logger.info(f"Shutting down {settings.APP_NAME}")