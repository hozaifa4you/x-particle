from metatrader.account_info import account_info
from metatrader.orders import (
    active_positions,
    pending_orders,
    deals_history_count,
    deals_details,
    deals_history_list,
)
from metatrader.market_data import candle_data, symbol_info, tradeable_symbols
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

    permission = tradeable_symbols()
    print(permission)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
