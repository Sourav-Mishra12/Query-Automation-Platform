from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/live")
def liveness():
    return {
        "status": "alive",
    }


@router.get("/ready")
def readiness():
    """
    Later we'll check:

    - Database
    - Redis
    - Plugins
    - Metadata Repository
    - AI Providers
    """

    return {
        "status": "ready",
    }