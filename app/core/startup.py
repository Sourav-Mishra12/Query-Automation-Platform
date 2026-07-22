from app.core.logging import logger
from app.core.config import settings


def startup():
    logger.info(f"{settings.APP_NAME} started successfully.")
    logger.info(f"Environment : {settings.ENVIRONMENT}")
    logger.info(f"Version     : {settings.APP_VERSION}")