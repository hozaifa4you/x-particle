from typing import List, TypedDict, Annotated
from llm.groq import llm
from tools.tavily import google_search
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages, StateGraph
from langgraph.prebuilt import ToolNode


class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]


async def agent_node(state: State):
    messages = state["messages"]

    print(messages)
    print(state.__dict__)

    response = await llm.ainvoke(messages, tools=[google_search])

    return {"messages": [response]}


async def build_graph():
    graph = StateGraph(State)

    # add agent and tool nodes
    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode([google_search]))

    # routing: agent -> tools -> agent -> tools
    graph.add_edge("agent", "tools")
    graph.add_edge("tools", "agent")

    # start at the agent
    graph.set_entry_point("agent")

    return graph.compile()
