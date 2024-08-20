from datetime import datetime, timedelta

from pytrade.enum.Action import Action
from pytrade.enum.Contract import Contract
from pytrade.model.Signal import Signal
from pytrade.schema.SignalDto import SignalDto

def test_signal_lt():
    s1 = Signal(SignalDto("AAPL", 10, Action.Buy, Contract.Call, datetime.now()))
    s2 = Signal(SignalDto("XOM", 333, Action.Sell, Contract.Call, datetime.now() + timedelta(hours=1)))
    s3 = Signal(SignalDto("KO", 67, Action.Sell, Contract.Put, datetime.now() + timedelta(days=2)))

    assert s1 < s2 < s3
    