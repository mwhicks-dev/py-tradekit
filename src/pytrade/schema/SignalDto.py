from datetime import datetime

from pydantic import BaseModel

from pytrade.enum import Action, Contract

class SignalDto(BaseModel):

    ticker: str
    volume: int
    action: Action
    contract: Contract
    time: datetime