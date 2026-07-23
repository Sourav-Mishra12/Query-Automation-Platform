from sqlalchemy import String , Float , DECIMAL , Date
from datetime import date 

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Trade(Base):
    __tablename__ = "Trade"

    TradeId: Mapped[int] = mapped_column(primary_key=True)

    CompanyId : Mapped[int]

    DealerId : Mapped[int]

    TradeDate : Mapped[date] = mapped_column(Date)

    OpeningPrice : Mapped[float] 

    ClosingPrice : Mapped[float]

    HighPrice : Mapped[float]

    LowPrice : Mapped[float]

    Quantity : Mapped[int]

    TradeValue : Mapped[DECIMAL] = mapped_column(DECIMAL(18,2))