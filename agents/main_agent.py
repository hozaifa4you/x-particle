from langchain.messages import AnyMessage, SystemMessage, ToolMessage
from typing_extensions import TypedDict, Annotated
import operator
from typing import Literal
from langgraph.graph import StateGraph, START, END
from llm.groq import llm as model
from agents.system_prompt import system_prompt
from tools.tools import (
    tavily_web_search_tool,
    close_order_tool,
    modify_order_tool,
    send_order_tool,
    get_account_info_tool,
    get_candle_data_tools,
    get_candle_data_tools as get_candle_data_tool,
    symbol_info_tool,
    tradeable_symbols_tool as get_tradeable_symbols_tool,
    get_active_orders_count_tool,
    get_deals_details_tool,
    get_active_positions_tool,
    get_deals_history_count_tool,
    get_pending_orders_count_tool,
    get_pending_orders_tool,
    get_deals_history_list_tool,
    get_terminal_info_tool,
    is_trading_allowed_tool,
)


tools = [
    tavily_web_search_tool,
    is_trading_allowed_tool,
    close_order_tool,
    modify_order_tool,
    send_order_tool,
    get_account_info_tool,
    get_candle_data_tools,
    get_candle_data_tool,  # Register alias for LLM compatibility
    symbol_info_tool,
    get_tradeable_symbols_tool,  # Register alias for LLM compatibility
    get_active_orders_count_tool,
    get_deals_details_tool,
    get_active_positions_tool,
    get_deals_history_count_tool,
    get_pending_orders_count_tool,
    get_pending_orders_tool,
    get_deals_history_list_tool,
    get_terminal_info_tool,
]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)


class MessageState(TypedDict):
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

    import json

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        # Always stringify the observation for LLM compatibility
        try:
            content = json.dumps(observation, ensure_ascii=False)
        except Exception:
            content = str(observation)
        result.append(ToolMessage(content=content, tool_call_id=tool_call["id"]))

    return {"messages": result}


def should_continue(state: MessageState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # Debug: print the last message to see if tool_calls is present
    # print(
    #     str(last_message).encode("ascii", errors="replace").decode(),
    # )

    # if the llm makes a tool call, then perform an action
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tool_node"

    # otherwise, we are done
    return END


# workflow builder
agent_builder = StateGraph(MessageState)

# add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# add edges
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
agent_builder.add_edge("tool_node", "llm_call")

# compile the agent
agent = agent_builder.compile()
