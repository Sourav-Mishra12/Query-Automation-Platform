from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)



# from sqlalchemy import text
# from app.core.database import engine

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT DB_NAME()"))
#     print("Connected to:", result.scalar())   for testing purpose 