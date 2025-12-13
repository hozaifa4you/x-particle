from langchain.messages import HumanMessage
from agents.main_agent import agent
from metatrader.account_info import account_info
from metatrader.current_orders import current_orders


async def main():
    orders = current_orders()
    print(orders)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
