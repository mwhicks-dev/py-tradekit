from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from enum.Action import Action
from enum.Contract import Contract

class TradeDto(BaseModel):

    ticker: str
    volume: int
    action: Action
    contract: Contract
    time: datetime
    value: Decimal