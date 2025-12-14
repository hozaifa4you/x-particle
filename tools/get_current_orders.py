from langchain.tools import tool
from metatrader.orders import active_positions, pending_orders


@tool
def get_pending_orders_tool():
    """
    Retrieves all conditional trade orders (e.g., Buy Limit, Sell Stop)
    that are currently pending execution on the MT5 account.

    Returns: A Pandas DataFrame of pending orders with key columns (ticket, symbol,
    type_str, volume, price_open), or a string detailing the failure reason.

    Use this tool when the user asks to see their limit, stop, or conditional orders.
    """
    orders = pending_orders()
    return orders


@tool
def get_active_positions_tool():
    """
    Retrieves all open trades (positions) that are currently running in the market
    and incurring a live floating profit/loss on the MT5 account.

    Returns: A Pandas DataFrame of active positions with key columns (ticket, symbol,
    type_str, volume, price_open, profit), or a string detailing the failure reason.

    Use this tool when the user asks for their open trades, running trades, or current account exposure.
    """

    orders = active_positions()
    return orders
