from metatrader.account_info import account_info
from metatrader.current_orders import active_positions, pending_orders
from metatrader.historical_orders import get_history_deals, get_history_orders
from metatrader.market_data import get_market_data


async def main():
    ac_info = account_info()
    orders = active_positions()
    pen_orders = pending_orders()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
