import MetaTrader5 as mt5
import pandas as pd
from typing import Optional

from .common import ensure_mt5_connection


def pending_orders():
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    orders = mt5.orders_get()
    mt5.shutdown()

    if orders is None or len(orders) == 0:
        return "No active pending orders found on the account."

    df = pd.DataFrame(list(orders), columns=orders[0]._asdict().keys())
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.drop(
        ["time_update", "time_msc", "time_update_msc", "external_id"],
        axis=1,
        inplace=True,
    )

    return df


def active_positions():
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    positions = mt5.positions_get()
    mt5.shutdown()

    if positions is None or len(positions) == 0:
        return "No active open positions (running trades) found on the account."

    # display these positions as a table using pandas.DataFrame
    df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.drop(
        ["time_update", "time_msc", "time_update_msc", "external_id"],
        axis=1,
        inplace=True,
    )

    return df


def total_pending_orders() -> Optional[int | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    order_count = mt5.orders_total()
    mt5.shutdown()

    return order_count


def total_active_orders() -> Optional[int | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    order_count = mt5.positions_total()
    mt5.shutdown()

    return order_count
