import MetaTrader5 as mt5
import pandas as pd
from typing import Optional
from datetime import datetime, timedelta

from .common import ensure_mt5_connection

# print("\nAvailable columns:", pd_orders_frame.columns.tolist())


def pending_orders():
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    pd_orders = mt5.orders_get()

    if pd_orders is None or len(pd_orders) == 0:
        mt5.shutdown()
        return "Currently on pending orders"

    pd_orders_frame = pd.DataFrame([order._asdict() for order in pd_orders])
    pd_orders_frame["time_setup"] = pd.to_datetime(
        pd_orders_frame["time_setup"], unit="s"
    )
    pd_orders_frame["time_setup_msc"] = pd.to_datetime(
        pd_orders_frame["time_setup_msc"], unit="ms"
    )

    display_columns = [
        "ticket",
        "symbol",
        "time_setup",
        "time_setup_msc",
        "time_done",
        "time_done_msc",
        "time_expiration",
        "type",
        "type_time",
        "type_filling",
        "state",
        "magic",
        "position_id",
        "position_by_id",
        "reason",
        "volume_initial",
        "volume_current",
        "price_open",
        "sl",
        "tp",
        "price_current",
        "price_stoplimit",
        "comment",
        "external_id",
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
    if positions is None or len(positions) == 0:
        mt5.shutdown()
        return "Currently no active positions"

    active_positions_frame = pd.DataFrame(
        [position._asdict() for position in positions]
    )

    active_positions_frame["time"] = pd.to_datetime(
        active_positions_frame["time"], unit="s"
    )
    active_positions_frame["time_msc"] = pd.to_datetime(
        active_positions_frame["time_msc"], unit="ms"
    )

    display_columns = [
        "ticket",
        "symbol",
        "time",
        "time_msc",
        "time_update",
        "time_update_msc",
        "type",
        "magic",
        "identifier",
        "reason",
        "volume",
        "price_open",
        "sl",
        "tp",
        "price_current",
        "swap",
        "profit",
        "comment",
        "external_id",
    ]

    active_positions_display = active_positions_frame[display_columns]
    data = active_positions_display.to_string(index=False)

    mt5.shutdown()
    return data


def pending_orders_count() -> Optional[int | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    order_count = mt5.orders_total()
    mt5.shutdown()

    return order_count


def active_orders_count() -> Optional[int | str]:
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    order_count = mt5.positions_total()
    mt5.shutdown()

    return order_count


def deals_history_count(prev_days: int):
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    from_date = datetime.now() - timedelta(days=prev_days)
    to_date = datetime.now()

    count = mt5.history_deals_total(from_date, to_date)
    mt5.shutdown()

    return count


def deals_history_list(prev_days: int):
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    from_date = datetime.now() - timedelta(days=prev_days)
    to_date = datetime.now()

    deals_list = mt5.history_deals_get(from_date, to_date, group="*USD*")
    deals_list_frame = pd.DataFrame(
        list(deals_list), columns=deals_list[0]._asdict().keys()
    )
    deals_list_frame["time"] = pd.to_datetime(deals_list_frame["time"], unit="s")

    mt5.shutdown()
    return deals_list_frame.to_string(index=False)


def deals_details(ticket: str | int):
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    details = mt5.history_deals_get(ticket=int(ticket))

    if details is None or len(details) == 0:
        mt5.shutdown()
        return "No deals found for this ticket"

    deals_list = [deal._asdict() for deal in details]

    mt5.shutdown()
    return deals_list
