from abc import ABC, abstractmethod

from pytrade.schema import HistoricalQuery, HistoricalDataDto, ValueDto

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