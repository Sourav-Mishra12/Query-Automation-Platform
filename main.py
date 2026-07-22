from fastapi import FastAPI

from app.core.config import settings
from app.core.startup import startup
from app.core.exceptions import register_exception_handlers
from app.core.lifespan import lifespan
from app.api.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

register_exception_handlers(app)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    } 





# @app.get("/test")
# def test():
#      raise Exception("DAMNNNNN") just checking but what forgot so will write later :) 


# from fastapi import Depends
# from sqlalchemy import text
# from sqlalchemy.orm import Session

# from app.core.dependencies import get_db


# @app.get("/health/db")
# def database_health(db: Session = Depends(get_db)):
#     db.execute(text("SELECT 1"))
#     return {
#         "database": "connected"
#     }   will rewrite later when have a DB running or else code goes brrrrr