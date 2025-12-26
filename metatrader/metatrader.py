import MetaTrader5 as mt5
import pandas as pd
from typing import Optional, Literal
from datetime import datetime, timedelta
from dataclasses import dataclass
from .common import ensure_mt5_connection, order_type_map


@dataclass
class OrderRequest:
    """Order request configuration"""

    symbol: str
    volume: float
    order_type: Literal[
        "BUY", "SELL", "BUY_LIMIT", "SELL_LIMIT", "BUY_STOP", "SELL_STOP"
    ]
    sl_points: Optional[int] = None  # Stop loss in points
    tp_points: Optional[int] = None  # Take profit in points
    price: Optional[float] = None  # For pending orders
    deviation: int = 20
    magic: int = 234000
    comment: str = "Python order"


def send_order(order_request: OrderRequest):
    """
    Send a trading order to MT5

    Args:
        order_request: OrderRequest object with order parameters

    Returns:
        dict: Order result with status and details
    """
    connected, error = ensure_mt5_connection()
    if not connected:
        return error

    # get symbol info
    symbol_info = mt5.symbol_info(order_request.symbol)
    if symbol_info is None:
        mt5.shutdown()
        return {
            "success": False,
            "error": f"The symbol {order_request.symbol} is not found.",
        }

    # Check the symbol is visible in market watch
    if not symbol_info.visible:
        # Try to enable it
        if not mt5.symbol_select(order_request.symbol, True):
            mt5.shutdown()
            return {
                "success": False,
                "error": f"The symbol {order_request.symbol} is not visible and cannot be enabled.",
            }

    # get current tick
    tick = mt5.symbol_info_tick(order_request.symbol)
    if tick is None:
        mt5.shutdown()
        return {
            "success": False,
            "error": f"Failed to get tick for {order_request.symbol}",
        }

    mt5_order_type = order_type_map.get(order_request.order_type)
    if mt5_order_type is None:
        mt5.shutdown()
        return {
            "success": False,
            "error": f"Invalid order type: {order_request.order_type}",
        }

    # Set price based on order type
    if order_request.order_type == "BUY":
        price = tick.ask
    elif order_request.order_type == "SELL":
        price = tick.bid
    else:
        price = order_request.price if order_request.price else tick.ask

    # Calculate SL and TP
    point = symbol_info.point
    if order_request.order_type in ["BUY", "BUY_LIMIT", "BUY_STOP"]:
        sl = (
            price - (order_request.sl_points * point)
            if order_request.sl_points
            else 0.0
        )
        tp = (
            price + (order_request.tp_points * point)
            if order_request.tp_points
            else 0.0
        )
    else:
        sl = (
            price + (order_request.sl_points * point)
            if order_request.sl_points
            else 0.0
        )
        tp = (
            price - (order_request.tp_points * point)
            if order_request.tp_points
            else 0.0
        )

    # Determine the correct filling mode
    filling_type = symbol_info.filling_mode

    # Check which filling modes are supported
    if filling_type & 2 == 2:  # FOK (Fill or Kill)
        type_filling = mt5.ORDER_FILLING_FOK
    elif filling_type & 1 == 1:  # IOC (Immediate or Cancel)
        type_filling = mt5.ORDER_FILLING_IOC
    elif filling_type & 4 == 4:  # RETURN (Return unfilled)
        type_filling = mt5.ORDER_FILLING_RETURN
    else:
        type_filling = mt5.ORDER_FILLING_RETURN  # Default fallback

    # actual order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": order_request.symbol,
        "volume": order_request.volume,
        "type": mt5_order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": order_request.deviation,
        "magic": order_request.magic,
        "comment": order_request.comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": type_filling,  # Use the auto-detected filling mode!
    }

    # Check the order first
    result = mt5.order_check(request)
    if result is None:
        mt5.shutdown()
        return {
            "success": False,
            "error": "Order check failed",
            "error_code": mt5.last_error(),
        }

    # ===== FIX: For order_check, retcode 0 means success! =====
    if result.retcode != 0:
        mt5.shutdown()
        return {
            "success": False,
            "error": f"Order check failed: {result.comment}",
            "retcode": result.retcode,
        }
    # ==========================================================

    # Send order
    result = mt5.order_send(request)

    if result is None:
        mt5.shutdown()
        return {
            "success": False,
            "error": "Order send failed",
            "error_code": mt5.last_error(),
        }

    # ===== For order_send, retcode 10009 means success =====
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        mt5.shutdown()
        return {
            "success": False,
            "error": f"Order failed: {result.comment}",
            "retcode": result.retcode,
            "result": result._asdict(),
        }
    # ======================================================

    # Success
    mt5.shutdown()
    return {
        "success": True,
        "ticket": result.order,
        "volume": result.volume,
        "price": result.price,
        "bid": result.bid,
        "ask": result.ask,
        "comment": result.comment,
        "request_id": result.request_id,
        "retcode": result.retcode,
        "deal": result.deal,
        "result": result._asdict(),
    }
