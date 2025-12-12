from langchain.messages import HumanMessage
from agents.main_agent import agent


async def main():
    print("Building agent graph...")
    messages = [HumanMessage(content="What is the weather in New York?")]
    messages = agent.invoke({"messages": messages})

    print(messages["messages"][-1].content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
