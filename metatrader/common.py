import MetaTrader5 as mt5
from config.environments import config


def ensure_mt5_connection():
    """Initializes MT5 connection if not already initialized."""
    if not mt5.initialize():
        error_code = mt5.last_error()
        return None, f"Failed to initialize MT5. Error code: {error_code}"
    return True, None


order_type_map = {
    "BUY": mt5.ORDER_TYPE_BUY,
    "SELL": mt5.ORDER_TYPE_SELL,
    "BUY_LIMIT": mt5.ORDER_TYPE_BUY_LIMIT,
    "SELL_LIMIT": mt5.ORDER_TYPE_SELL_LIMIT,
    "BUY_STOP": mt5.ORDER_TYPE_BUY_STOP,
    "SELL_STOP": mt5.ORDER_TYPE_SELL_STOP,
}
