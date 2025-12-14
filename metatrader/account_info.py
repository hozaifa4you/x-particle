import MetaTrader5 as mt5
from typing import Optional
from .common import ensure_mt5_connection


def account_info() -> Optional[mt5.AccountInfo]:
    """
    Connect to MetaTrader 5 and retrieve current trading account information.

    This function initializes the MT5 terminal connection (if not already connected),
    fetches the full account details, and returns them as an mt5.AccountInfo namedtuple.

    Returns:
        Optional[mt5.AccountInfo]:
            - On success: An AccountInfo object containing fields like:
                login, balance, equity, margin, margin_free, margin_level,
                leverage, currency, profit, name, server, trade_allowed, etc.
            - On failure: None (connection or data retrieval failed)

    Important fields for trading decisions:
        - balance: Current account balance (float)
        - equity: Balance + floating profit/loss (float)
        - margin: Currently used margin (float)
        - margin_free: Available margin for new positions (float)
        - margin_level: Margin level in % (float or None if no positions)
        - leverage: Account leverage (e.g., 100, 500, 1000) (int)
        - profit: Current unrealized P/L from open positions (float)
        - currency: Account currency (e.g., 'USD')

    Note: This function automatically handles initialization and prints errors for debugging.
    Always check if the result is not None before using the data.
    """

    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    info = mt5.account_info()
    if info is None:
        print("Error code:", mt5.last_error())
        return None

    return info
