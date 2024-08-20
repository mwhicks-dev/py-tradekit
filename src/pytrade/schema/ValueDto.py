from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

class ValueDto(BaseModel):

    ticker: str
    time: datetime
    value: Decimal