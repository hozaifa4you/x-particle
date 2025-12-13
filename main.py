from langchain.messages import HumanMessage
from agents.main_agent import agent
from metatrader.account_info import account_info


async def main():
    info = account_info()
    print(info)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
