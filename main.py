from agents.main_agent import agent
from langchain.messages import HumanMessage


def main():
    messages = [HumanMessage(content="Analyze and trade")]

    llm_call = agent.invoke(
        {
            "messages": messages,
        }
    )

    # Instead of print(messages), use safe print for unicode (ascii fallback)
    # Show only the latest message content
    # last_message = messages[-1]
    # print(
    #     str(getattr(last_message, "content", last_message))
    #     .encode("ascii", errors="replace")
    #     .decode()
    # )

    print(llm_call["messages"][0].content)


if __name__ == "__main__":
    main()
