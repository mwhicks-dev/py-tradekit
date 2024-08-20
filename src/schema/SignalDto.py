from datetime import datetime

from pydantic import BaseModel

from enum.Action import Action
from enum.Contract import Contract

class SignalDto(BaseModel):

    ticker: str
    volume: int
    action: Action
    contract: Contract
    time: datetime