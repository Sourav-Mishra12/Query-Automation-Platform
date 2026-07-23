from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Company(Base):
    __tablename__ = "Company"

    CompanyId: Mapped[int] = mapped_column(primary_key=True)

    CompanyName: Mapped[str] = mapped_column(String(200))

    Symbol: Mapped[str] = mapped_column(String(50))

    Sector : Mapped[str] = mapped_column(String(50))