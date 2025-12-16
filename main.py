from metatrader.account_info import account_info
from metatrader.orders import (
    active_positions,
    pending_orders,
    total_pending_orders,
    total_active_orders,
)
from metatrader.historical_orders import get_history_deals, get_history_orders
from metatrader.market_data import candle_data, symbol_info
from metatrader.common import ensure_mt5_connection
import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd


async def main():
    connected, error = ensure_mt5_connection()
    if not connected:
        print(error)
        quit()

    symbol = "EURUSD_o"

    data = pending_orders()
    print(data)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
