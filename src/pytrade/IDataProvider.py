from abc import ABC, abstractmethod

from schema.ValueDto import ValueDto
from schema.HistoricalQuery import HistoricalQuery
from schema.HistoricalDataDto import HistoricalDataDto

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