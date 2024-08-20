from datetime import datetime, timedelta

from pytrade.enum import Action, Contract
from pytrade.model import Signal
from pytrade.schema import SignalDto

def test_signal_lt():
    s1 = Signal(SignalDto(ticker="AAPL", 
        volume=10, action=Action.Buy, 
        contract=Contract.Call, time=datetime.now()))
    s2 = Signal(SignalDto(ticker="XOM", 
        volume=333, action=Action.Sell, 
        contract=Contract.Call, time=datetime.now() + timedelta(hours=1)))
    s3 = Signal(SignalDto(ticker="KO", 
        volume=67, action=Action.Sell, 
        contract=Contract.Put, time=datetime.now() + timedelta(days=2)))

    assert s1 < s2 < s3
    