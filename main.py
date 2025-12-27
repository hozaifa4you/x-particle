from agents.main_agent import agent
from langchain.messages import HumanMessage


def main():
    messages = [HumanMessage(content="Analyze and trade")]

    messages = agent.invoke({"messages": messages})

    # Instead of print(messages), use safe print for unicode (ascii fallback)
    print(str(messages).encode("ascii", errors="replace").decode())


if __name__ == "__main__":
    main()
