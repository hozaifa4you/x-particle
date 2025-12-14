import MetaTrader5 as mt5
import pandas as pd
from .common import ensure_mt5_connection
from typing import Optional, Dict


def candle_data(
    symbol: str, timeframe: int, initial_bar_index: int, number_of_bars: int
):
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    rates = mt5.copy_rates_from_pos(
        symbol, timeframe, initial_bar_index, number_of_bars
    )
    rates_frame = pd.DataFrame(rates)
    # convert time in seconds into the datetime format
    rates_frame["time"] = pd.to_datetime(rates_frame["time"], unit="s")

    return rates_frame


def get_symbol_info(symbol: str) -> Optional[Dict | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    symbol_info = mt5.symbol_info(symbol)
    mt5.shutdown()
    if symbol_info == None:
        return "Symbol info not found"

    return symbol_info._asdict()
