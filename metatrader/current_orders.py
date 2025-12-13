import MetaTrader5 as mt5
import pandas as pd

from .common import ensure_mt5_connection


def pending_orders():
    """
    Retrieves all conditional trade orders (e.g., Buy Limit, Sell Stop)
    that are currently pending execution on the MT5 account.

    Returns: A Pandas DataFrame of pending orders with key columns (ticket, symbol,
    type_str, volume, price_open), or a string detailing the failure reason.

    Use this tool when the user asks to see their limit, stop, or conditional orders.
    """
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    orders = mt5.orders_get()
    mt5.shutdown()

    if orders is None or len(orders) == 0:
        return "No active pending orders found on the account."

    orders_df = pd.DataFrame(list(orders))

    type_map = {
        mt5.ORDER_TYPE_BUY_LIMIT: "BUY_LIMIT",
        mt5.ORDER_TYPE_SELL_LIMIT: "SELL_LIMIT",
        mt5.ORDER_TYPE_BUY_STOP: "BUY_STOP",
        mt5.ORDER_TYPE_SELL_STOP: "SELL_STOP",
    }
    orders_df["type_str"] = orders_df["type"].map(type_map)
    orders_df["time_setup"] = pd.to_datetime(orders_df["time_setup"], unit="s")

    return orders_df[
        [
            "ticket",
            "time_setup",
            "symbol",
            "type_str",
            "volume_initial",
            "price_open",
            "sl",
            "tp",
        ]
    ].to_string(index=False)


def active_positions():
    """
    Retrieves all open trades (positions) that are currently running in the market
    and incurring a live floating profit/loss on the MT5 account.

    Returns: A Pandas DataFrame of active positions with key columns (ticket, symbol,
    type_str, volume, price_open, profit), or a string detailing the failure reason.

    Use this tool when the user asks for their open trades, running trades, or current account exposure.
    """
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    positions = mt5.positions_get()
    mt5.shutdown()

    if positions is None or len(positions) == 0:
        return "No active open positions (running trades) found on the account."

    # Process into a clean DataFrame for the LLM
    positions_df = pd.DataFrame(list(positions))

    # Map position types
    type_map = {
        mt5.POSITION_TYPE_BUY: "BUY (LONG)",
        mt5.POSITION_TYPE_SELL: "SELL (SHORT)",
    }
    positions_df["type_str"] = positions_df["type"].map(type_map)
    positions_df["time"] = pd.to_datetime(positions_df["time"], unit="s")

    return positions_df[
        [
            "ticket",
            "time",
            "symbol",
            "type_str",
            "volume",
            "price_open",
            "profit",
            "sl",
            "tp",
        ]
    ].to_string(index=False)
