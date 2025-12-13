import MetaTrader5 as mt5


def ensure_mt5_connection():
    """Initializes MT5 connection if not already initialized."""
    if not mt5.initialize():
        error_code = mt5.last_error()
        return None, f"Failed to initialize MT5. Error code: {error_code}"
    return True, None
