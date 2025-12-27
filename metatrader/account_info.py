import MetaTrader5 as mt5
from .common import ensure_mt5_connection
from datetime import datetime
from config.environments import config


def account_info() -> dict:
    connected, error = ensure_mt5_connection()
    if not connected:
        return {"success": False, "error": error}

    info = mt5.account_info()
    if info is None:
        return {
            "success": False,
            "error": "Failed to retrieve account information.",
        }

    return info._asdict()


def terminal_info():
    connected, error = ensure_mt5_connection()
    if not connected:
        return {"success": False, "error": error}

    info = mt5.terminal_info()
    if info is None:
        return {
            "success": False,
            "message": "Failed to retrieve terminal information.",
            "error": mt5.last_error(),
        }

    return info._asdict()


def allow_trading():
    off_day = config.OFF_DAYS
    current_day = datetime.now().strftime("%A")

    if current_day in off_day:
        return {
            "trading_allowed": False,
            "message": f"Trading is not allowed on {current_day}s. Because it's an off day.",
        }

    return {"trading_allowed": True, "message": "Trading is allowed today."}
