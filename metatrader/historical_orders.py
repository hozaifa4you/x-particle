import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta
import pytz
from .common import ensure_mt5_connection


def get_history_orders(days_back: int = 30):
    """Retrieves all historical orders (filled, cancelled, expired) from the MT5 account history."""
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    timezone = pytz.timezone("Etc/UTC")
    today = datetime.now(timezone)
    date_from = today - timedelta(days=days_back)

    history_orders = mt5.history_orders_get(date_from, today)
    mt5.shutdown()

    if history_orders is None:3
        return f"Failed to retrieve historical orders. MT5 Error: {mt5.last_error()}"
    elif len(history_orders) == 0:
        return f"No historical orders found in the last {days_back} days."

    orders_df = pd.DataFrame(list(history_orders))
    orders_df["time_done"] = pd.to_datetime(orders_df["time_done"], unit="s")

    # Map status and type for readability
    state_map = {
        mt5.ORDER_STATE_CANCELED: "CANCELED",
        mt5.ORDER_STATE_FILLED: "FILLED",
        mt5.ORDER_STATE_EXPIRED: "EXPIRED",
    }
    type_map = {
        mt5.ORDER_TYPE_BUY: "BUY_MARKET",
        mt5.ORDER_TYPE_SELL: "SELL_MARKET",
        mt5.ORDER_TYPE_BUY_LIMIT: "BUY_LIMIT",
        mt5.ORDER_TYPE_SELL_STOP: "SELL_STOP",
    }
    orders_df["state_str"] = orders_df["state"].map(state_map).fillna("Other")
    orders_df["type_str"] = orders_df["type"].map(type_map).fillna("Other")

    return orders_df[
        [
            "ticket",
            "time_done",
            "symbol",
            "type_str",
            "state_str",
            "price_open",
            "volume_initial",
        ]
    ].to_string(index=False)


def get_history_deals(days_back: int = 30):
    """Retrieves all historical deals (executed transactions) from the MT5 account history."""
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    timezone = pytz.timezone("Etc/UTC")
    today = datetime.now(timezone)
    date_from = today - timedelta(days=days_back)

    history_deals = mt5.history_deals_get(date_from, today)
    mt5.shutdown()

    if history_deals is None:
        return f"Failed to retrieve historical deals. MT5 Error: {mt5.last_error()}"
    elif len(history_deals) == 0:
        return f"No historical deals (executions) found in the last {days_back} days."

    deals_df = pd.DataFrame(list(history_deals))
    deals_df["time"] = pd.to_datetime(deals_df["time"], unit="s")

    # Map deal types
    type_map = {
        mt5.DEAL_TYPE_BUY: "BUY_EXECUTION",
        mt5.DEAL_TYPE_SELL: "SELL_EXECUTION",
    }
    deals_df["type_str"] = deals_df["type"].map(type_map).fillna("Other")

    return deals_df[
        [
            "ticket",
            "time",
            "symbol",
            "type_str",
            "volume",
            "price",
            "profit",
            "commission",
        ]
    ].to_string(index=False)
