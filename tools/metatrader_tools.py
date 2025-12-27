from metatrader.metatrader import send_order, close_order, modify_order
from langchain.tools import tool
from config.environments import config


@tool
def send_order_tool(
    symbol,
    order_type,
    deviation,
    volume,
    sl_points=None,
    tp_points=None,
    price=None,
    comment="Close by X Particle",
):
    """
    Place a new trade/order in MetaTrader 5.

    Args:
        symbol (str): Symbol name (e.g., 'EURUSDm'). # Use `tradeable_symbols_tool` to get a list of available symbols.
        order_type (str): Order type (Only "BUY", "SELL", "BUY_LIMIT", "SELL_LIMIT", "BUY_STOP", "SELL_STOP").
        deviation (int): Max price deviation allowed.
        volume (float): Trade volume.
        sl_points (int, optional): Stop loss in points.
        tp_points (int, optional): Take profit in points.
        price (float, optional): Price for pending orders.
        comment (str, optional): Order comment.

    Returns:
        dict: Result of the order operation (success, error, ticket, etc.)
    """

    return send_order(
        symbol=symbol,
        volume=volume,
        price=price,
        sl_points=sl_points,
        tp_points=tp_points,
        order_type=order_type,
        deviation=deviation,
        comment=comment,
    )


@tool
def close_order_tool(
    ticket: int,
    deviation: int = 20,
    magic: int = 99,
    comment: str = "Close by X Particle",
):
    """`
    Close an open position by ticket number.

    Args:
        ticket (int): The position/order ticket to close.
        deviation (int): Max price deviation allowed (default 20).
        magic (int): Magic number for the order (default 234000).
        comment (str): Comment for the close order.

    Returns:
        dict: Result of the close operation (success, error, etc.)
    """

    return close_order(ticket, deviation, magic, comment)


@tool
def modify_order_tool(
    ticket: int,
    sl: float | None = None,
    tp: float | None = None,
    deviation: int = 20,
    magic: int = config.MAGIC_NUMBER,
    comment: str = "Modify by X Particle",
):
    """
    Modify stop loss and/or take profit for an open position.

    Args:
        ticket (int): The position/order ticket to modify.
        sl (float): New stop loss price (None to leave unchanged).
        tp (float): New take profit price (None to leave unchanged).
        deviation (int): Max price deviation allowed (default 20).
        magic (int): Magic number for the order (default 99).
        comment (str): Comment for the modify order.

    Returns:
        dict: Result of the modify operation (success, error, etc.)
    """

    return modify_order(
        ticket=ticket,
        comment=comment,
        sl=sl,
        tp=tp,
        deviation=deviation,
        magic=magic,
    )
