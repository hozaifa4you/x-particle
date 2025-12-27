from metatrader.market_data import candle_data, symbol_info, tradeable_symbols
from langchain.tools import tool
from typing import Optional


@tool
def get_candel_data_tools(
    symbol: str, timeframe: int, initial_bar_index: int = 0, number_of_bars: int = 100
):
    """
    Retrieve historical candle (OHLCV) data for a symbol and timeframe.

    Args:
        symbol (str): Symbol name (e.g., 'EURUSDm'). `tradeable_symbols_tool` can be used to get a list of available symbols.
        timeframe (int):
            MT5 timeframe constant (e.g., mt5.TIMEFRAME_M1-> 1 minute -> 1):
                1: 1 minute
                5: 5 minutes
                15: 15 minutes
                30: 30 minutes
                16385: 1 hour
                16386: 4 hours
                16401: 1 day
                16416: 1 week
                16432: 1 month
        initial_bar_index (int): Start index (0 = most recent); default is 0
        number_of_bars (int): Number of bars to fetch; default is 100

    Returns:
        list of dict: Each dict contains keys: time, open, high, low, close, tick_volume, spread, real_volume
    Example:
        [
            {"time": "2025-12-26 16:05:00", "open": 1.17761, "high": 1.17765, ...},
            ...
        ]
    """
    df = candle_data(symbol, timeframe, initial_bar_index, number_of_bars)
    return df


@tool
def symbol_info_tool(symbol: str) -> Optional[dict | str]:
    """
    Retrieve detailed MetaTrader 5 symbol information as a dictionary.

    Args:
        symbol (str): Symbol name (e.g., 'EURUSD')

    Returns:
        dict: Symbol details (bid, ask, point, digits, spread, volume_min, volume_max, etc.)
    Example:
        {
            'symbol': 'EURUSD', 'bid': 1.17756, 'ask': 1.17758, 'point': 0.00001,
            'digits': 5, 'spread': 2, 'volume_min': 0.01, 'volume_max': 100.0,
            ... (other MetaTrader5 symbol fields)
        }
    """
    return symbol_info(symbol)


@tool
def tradeable_symbols_tool() -> Optional[list | str]:
    """
    Retrieve a list of all allowed/tradeable symbols and their details.

    Returns:
        list of dict: Each dict contains symbol info (symbol, bid, ask, digits, volume_min, etc.)
    Example:
        [
            {'symbol': 'EURUSD', 'bid': 1.17756, 'ask': 1.17758, ...},
            {'symbol': 'XAUUSD', 'bid': 2050.12, 'ask': 2050.34, ...},
            ...
        ]
    """
    return tradeable_symbols()
