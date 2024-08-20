from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

class HistoricalDataDto(BaseModel):

    ticker: str
    start: datetime
    end: datetime
    low: Decimal
    high: Decimal