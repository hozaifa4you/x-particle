from agents.main_agent import agent
from langchain.messages import HumanMessage


def main():
    messages = [HumanMessage(content="Hello! Analyze and trade accordingly.")]

    messages = agent.invoke({"messages": messages})
    for m in messages["messages"]:
        m.pretty_print()


if __name__ == "__main__":
    main()
