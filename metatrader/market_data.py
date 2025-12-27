import MetaTrader5 as mt5
import pandas as pd
from .common import ensure_mt5_connection
from typing import Optional, Dict
from config.environments import config


pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1500)


def candle_data(
    symbol: str, timeframe: int, initial_bar_index: int, number_of_bars: int
):
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    rates = mt5.copy_rates_from_pos(
        symbol, timeframe, initial_bar_index, number_of_bars
    )

    if rates is None or len(rates) == 0:
        mt5.shutdown()
        return []

    rates_frame = pd.DataFrame(rates)
    if "time" in rates_frame.columns:
        rates_frame["time"] = pd.to_datetime(rates_frame["time"], unit="s")
    mt5.shutdown()

    return rates_frame.to_dict(orient="records")


def symbol_info(symbol: str) -> Optional[Dict | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    _symbol_info = mt5.symbol_info(symbol)
    mt5.shutdown()
    if _symbol_info == None:
        return "Symbol info not found"

    return _symbol_info._asdict()


def tradeable_symbols() -> Optional[list | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    # Define your symbols
    my_symbols = config.SYMBOLS

    symbols_info = []

    for symbol in my_symbols:
        info = mt5.symbol_info(symbol)
        if info is not None:
            symbols_info.append(info._asdict())

    mt5.shutdown()
    return symbols_info
