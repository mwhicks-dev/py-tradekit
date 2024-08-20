from abc import ABC, abstractmethod
from datetime import datetime

from model.Signal import Signal

from schema.SignalDto import SignalDto
from schema.TradeDto import TradeDto

class Broker(ABC):

    signals: list[Signal] = []

    def push_signal(self, dto: SignalDto) -> None:
        self.signals.append(Signal(dto))
        self.signals.sort()

    async def _pop_signal(self) -> Signal:
        # wait until there is a signal to pop
        while not (len(self.signals) > 0 
                   and self.signals[0].time < datetime.now()):
            pass

        return self.signals.pop(0)
    
    @abstractmethod
    async def execute_next_signal(self) -> TradeDto:
        pass