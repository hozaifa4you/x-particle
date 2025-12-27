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
