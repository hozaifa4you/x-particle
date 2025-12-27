import MetaTrader5 as mt5
from .common import ensure_mt5_connection


def account_info():
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    info = mt5.account_info()
    if info is None:
        return {
            "success": False,
            "error": "Failed to retrieve account information.",
        }

    return info._asdict()
