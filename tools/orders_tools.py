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
    """
    Get the number of currently active/open orders in the MetaTrader 5 account.

    Returns:
        int: The count of active/open orders.
    Example:
        3
    """
    return active_orders_count()


@tool
def get_active_positions_tool():
    """
    Get a list of all currently active/open positions in the MetaTrader 5 account.

    Returns:
        list of dict: Each dict contains position details (ticket, symbol, volume, type, price_open, sl, tp, profit, etc.)
    Example:
        [
            {
                'ticket': 123456789,
                'symbol': 'EURUSDm',
                'volume': 0.1,
                'type': 0,  # 0=buy, 1=sell
                'price_open': 1.17756,
                'sl': 1.17600,
                'tp': 1.18000,
                'profit': 5.25,
                ...
            },
            ...
        ]
    """
    return active_positions()


@tool
def get_deals_details_tool(ticket: str | int):
    """
    Get detailed information about a specific deal (trade) by ticket number.

    Args:
        ticket (str | int): The deal ticket number.

    Returns:
        dict: Deal details (ticket, symbol, type, volume, price, profit, time, etc.)
    Example:
        {
            'ticket': 987654321,
            'symbol': 'EURUSDm',
            'type': 0,  # 0=buy, 1=sell
            'volume': 0.1,
            'price': 1.17756,
            'profit': 5.25,
            'time': '2025-12-27 14:32:00',
            ...
        }
    """
    return deals_details(ticket=ticket)


@tool
def get_deals_history_count_tool(prev_days: int):
    """
    Get the number of deals (trades) executed in the last N days.

    Args:
        prev_days (int): Number of previous days to look back for deal history.

    Returns:
        int: The count of deals executed in the given period.
    Example:
        12
    """
    return deals_history_count(prev_days=prev_days)


@tool
def get_deals_history_list_tool(prev_days: int = 30):
    """
    Get a list of all deals (trades) executed in the last N days.

    Args:
        prev_days (int, optional): Number of previous days to look back for deal history (default 30).

    Returns:
        list of dict: Each dict contains deal details (ticket, symbol, type, volume, price, profit, time, etc.)
    Example:
        [
            {
                'ticket': 987654321,
                'symbol': 'EURUSDm',
                'type': 0,  # 0=buy, 1=sell
                'volume': 0.1,
                'price': 1.17756,
                'profit': 5.25,
                'time': '2025-12-27 14:32:00',
                ...
            },
            ...
        ]
    """
    return deals_history_list(prev_days=prev_days)


@tool
def get_pending_orders_tool():
    """
    Get a list of all currently pending orders in the MetaTrader 5 account.

    Returns:
        list of dict: Each dict contains pending order details (ticket, symbol, type, price, volume, sl, tp, time_setup, etc.)
    Example:
        [
            {
                'ticket': 234567890,
                'symbol': 'EURUSDm',
                'type': 2,  # 2=buy limit, 3=sell limit, etc.
                'price': 1.17500,
                'volume': 0.1,
                'sl': 1.17400,
                'tp': 1.17800,
                'time_setup': '2025-12-27 15:00:00',
                ...
            },
            ...
        ]
    """
    return pending_orders()


@tool
def get_pending_orders_count_tool():
    """
    Get the number of currently pending orders in the MetaTrader 5 account.

    Returns:
        int: The count of pending orders.
    Example:
        2
    """
    return pending_orders_count()
