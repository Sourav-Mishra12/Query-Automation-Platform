from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Dealer(Base):
    __tablename__ = "Dealer"

    DealerId: Mapped[int] = mapped_column(primary_key=True)

    DealerName: Mapped[str] = mapped_column(String(200))

    Branch : Mapped[str] = mapped_column(String(50))