import MetaTrader5 as mt5
import pandas as pd
from typing import Optional

from .common import ensure_mt5_connection


def pending_orders():
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    pd_orders = mt5.orders_get()

    if pd_orders is None or len(pd_orders) == 0:
        mt5.shutdown()
        return "Currently on pending orders"

    # Convert to DataFrame - use _asdict() to preserve field names
    pd_orders_frame = pd.DataFrame([order._asdict() for order in pd_orders])
    # print(pd_orders_frame)

    # Now you can access columns by name
    pd_orders_frame["time_setup"] = pd.to_datetime(
        pd_orders_frame["time_setup"], unit="s"
    )
    pd_orders_frame["time_setup_msc"] = pd.to_datetime(
        pd_orders_frame["time_setup_msc"], unit="ms"
    )

    # Optional: Select and reorder specific columns for better display
    display_columns = [
        "ticket",
        "symbol",
        "type",
        "volume_current",
        "price_open",
        "sl",
        "tp",
        "price_current",
        "time_setup",
        "state",
        "comment",
    ]

    pd_orders_display = pd_orders_frame[display_columns]
    data = pd_orders_display.to_string(index=False)
    mt5.shutdown()

    return data


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
