from agent.agent import build_graph


async def main():
    app = build_graph()

    result = await app.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "What is the weather of Dhaka city today?"}
            ]
        }
    )

    final_message = result["messages"][-1]
    print(final_message)
