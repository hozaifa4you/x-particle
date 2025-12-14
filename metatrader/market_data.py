import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
from .common import ensure_mt5_connection


def get_market_data(symbol: str, timeframe, count: int):
    """
    Retrieves the most recent 'count' bars of market data for a given symbol and timeframe.

    Args:
        symbol (str): The trading symbol (e.g., 'EURUSD').
        timeframe: The MT5 timeframe constant (e.g., mt5.TIMEFRAME_H1).
        count (int): The number of recent bars to retrieve.

    Returns: A formatted string of a Pandas DataFrame, or a string detailing the error.
    """
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    print(symbol, timeframe, count)

    # 1. Retrieve the rates from the end of history (position 0, count X)
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    mt5.shutdown()

    if rates is None or len(rates) == 0:
        return f"Failed to retrieve data for {symbol} on timeframe {timeframe}. MT5 Error: {mt5.last_error()}"

    # 2. Convert to a Pandas DataFrame
    rates_frame = pd.DataFrame(rates)

    # 3. Format the time column for readability
    rates_frame["time"] = pd.to_datetime(rates_frame["time"], unit="s")

    # Optional: Set time as index
    rates_frame = rates_frame.set_index("time")

    # 4. Display the results
    timeframe_str = ""
    # A simple way to map common timeframes for display
    if timeframe == mt5.TIMEFRAME_H1:
        timeframe_str = "H1 (1 Hour)"
    elif timeframe == mt5.TIMEFRAME_M30:
        timeframe_str = "M30 (30 Minutes)"

    header = f"--- Last {count} {timeframe_str} Rates for {symbol} ---\n"

    return header + rates_frame.to_string(float_format="%.5f")


# --- EXAMPLE USAGE ---

# # Call the function to get the last 100 H1 candles for EURUSD
# result = get_market_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_H1, count=100)

# print(result)
