from abc import ABC, abstractmethod

from pytrade.schema import SignalDto

class IModel(ABC):

    @abstractmethod
    def generate_signals() -> tuple[SignalDto, ...]:
        pass