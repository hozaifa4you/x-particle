from metatrader.account_info import account_info
from metatrader.orders import (
    active_positions,
    pending_orders,
    total_pending_orders,
    total_active_orders,
)
from metatrader.historical_orders import get_history_deals, get_history_orders
from metatrader.market_data import candle_data, get_symbol_info
from metatrader.common import ensure_mt5_connection
import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd

pd.set_option("display.max_columns", 500)  # number of columns to be displayed
pd.set_option("display.width", 1500)  # max table width to display


async def main():
    connected, error = ensure_mt5_connection()
    if not connected:
        print(error)
        quit()

    data = candle_data("EURUSD_o", mt5.TIMEFRAME_H1, 0, 10)
    print(data)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
