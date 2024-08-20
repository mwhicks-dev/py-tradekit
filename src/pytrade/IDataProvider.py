from abc import ABC, abstractmethod

from pytrade.schema.ValueDto import ValueDto
from pytrade.schema.HistoricalQuery import HistoricalQuery
from pytrade.schema.HistoricalDataDto import HistoricalDataDto

class IDataProvider(ABC):

    @abstractmethod
    def get_value(self, ticker: str) -> ValueDto:
        pass

    @abstractmethod
    def get_historical_grains(self) -> tuple[str, ...]:
        pass

    @abstractmethod
    def get_historical_data(self, dto: HistoricalQuery) -> list[HistoricalDataDto]:
        pass