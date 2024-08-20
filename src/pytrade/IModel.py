from abc import ABC, abstractmethod

from pytrade.schema.SignalDto import SignalDto

class IModel(ABC):

    @abstractmethod
    def generate_signals() -> tuple[SignalDto, ...]:
        pass