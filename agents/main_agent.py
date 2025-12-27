from langchain.messages import AnyMessage, SystemMessage, ToolMessage
from typing_extensions import TypedDict, Annotated
import operator
from typing import Literal
from langgraph.graph import StateGraph, START, END
from llm.groq import model
from agents.system_prompt import system_prompt
from tools.tools import (
    close_order_tool,
    get_account_info_tool,
    get_active_orders_count_tool,
    get_active_positions_tool,
    get_candle_data_tools,
    get_deals_details_tool,
    get_deals_history_count_tool,
    get_deals_history_list_tool,
    get_pending_orders_count_tool,
    get_pending_orders_tool,
    is_trading_allowed_tool,
    modify_order_tool,
    get_terminal_info_tool,
    send_order_tool,
    symbol_info_tool,
    tradeable_symbols_tool,
    tavily_web_search_tool,
)


tools = [
    close_order_tool,
    get_account_info_tool,
    get_active_orders_count_tool,
    get_active_positions_tool,
    get_candle_data_tools,
    get_deals_details_tool,
    get_deals_history_count_tool,
    get_deals_history_list_tool,
    get_pending_orders_count_tool,
    get_pending_orders_tool,
    is_trading_allowed_tool,
    modify_order_tool,
    get_terminal_info_tool,
    send_order_tool,
    symbol_info_tool,
    tradeable_symbols_tool,
    tavily_web_search_tool,
]

tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int


def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [SystemMessage(content=system_prompt)] + state["messages"]
            )
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


def tool_node(state: dict):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))

    return {"messages": result}


def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:  # type: ignore
        return "tool_node"

    return END


# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()
