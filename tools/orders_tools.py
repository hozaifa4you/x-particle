from metatrader.orders import (
    active_orders_count,
    active_positions,
    deals_details,
    deals_history_count,
    deals_history_list,
    pending_orders,
    pending_orders_count,
)
from langchain.tools import tool


@tool
def get_active_orders_count_tool():
    return active_orders_count()


@tool
def get_active_positions_tool():
    return active_positions()


@tool
def get_deals_details_tool(ticket: str | int):
    return deals_details(ticket=ticket)


@tool
def get_deals_history_count_tool(prev_days: int):
    return deals_history_count(prev_days=prev_days)


@tool
def get_deals_history_list_tool():
    return deals_history_list(prev_days=30)


@tool
def get_pending_orders_tool():
    return pending_orders()


@tool
def get_pending_orders_count_tool():
    return pending_orders_count()
