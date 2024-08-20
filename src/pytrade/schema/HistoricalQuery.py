from datetime import datetime

from pydantic import BaseModel

class HistoricalQuery(BaseModel):

    ticker: str
    grain: str
    start: datetime
    end: datetime