import MetaTrader5 as mt5
from typing import Optional
from .common import ensure_mt5_connection


def account_info() -> Optional[mt5.AccountInfo]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    info = mt5.account_info()
    if info is None:
        print("Error code:", mt5.last_error())
        return None

    return info
