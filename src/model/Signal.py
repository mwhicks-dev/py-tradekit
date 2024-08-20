from datetime import datetime

from enum.Action import Action
from enum.Contract import Contract

from schema.SignalDto import SignalDto

class Signal:

    ticker: str
    volume: int
    action: Action
    contract: Contract
    time: datetime

    def __init__(self, dto: SignalDto):
        self.ticker = dto.ticker
        self.volume = dto.volume
        self.action = dto.action
        self.contract = dto.contract
        self.time = dto.time
    
    def __lt__(self, other) -> bool:
        return self.time < other.time