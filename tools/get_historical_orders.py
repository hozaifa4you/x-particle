from langchain.tools import tool
from metatrader.historical_orders import get_history_deals, get_history_orders


@tool
def get_historical_orders_tool(days_back: int = 30):
    """
    Fetches the account's historical **ORDER INSTRUCTIONS** (filled, cancelled, or expired)
    over the specified number of days (default 30). This is useful for analyzing
    why a trade did or did not execute.

    Args:
        days_back (int): The number of days of history to retrieve.

    Returns: A formatted table string of historical orders.
    """
    return get_history_orders(days_back=days_back)


@tool
def get_historical_deals_tool(days_back: int = 30):
    """
    Fetches the account's historical **DEALS** (final trade executions)
    over the specified number of days (default 30). This is the definitive record
    of all transactions and the final profit/loss for closed positions.

    Args:
        days_back (int): The number of days of history to retrieve.

    Returns: A formatted table string of historical deals, showing profit and commission.
    """
    return get_history_deals(days_back=days_back)
