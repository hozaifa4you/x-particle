# Copilot Instructions for x-particle AI Forex Trading Bot

## Project Overview
- **Purpose:** AI-powered, fully automated Forex trading bot using MetaTrader 5, LangChain, and LangGraph.
- **Key Pairs:** Only trades EURUSD, AUDUSD, GBPUSD, USDCAD, USDCHF, USDJPY, NZDUSD, and XAUUSD (Gold). Never interact with other symbols.
- **Architecture:**
  - `main.py`: Entry point, demonstrates order placement using abstractions.
  - `agents/`: Contains the main agent logic (`main_agent.py`) and the system prompt (`system_prompt.py`).
  - `metatrader/`: Handles all MT5 integration (order execution, market data, account info, etc.).
  - `tools/`: LangChain-compatible tools for agent use (account info, orders, market data, web search).
  - `config/`: Environment and API configuration.

## Agent & Workflow Patterns
- **Agent Loop:** Built with LangGraph. Alternates between LLM decision (`llm_call`) and tool execution (`tool_node`) until no further tool calls are needed.
- **System Prompt:** Strictly enforces risk management, symbol whitelist, and workflow (see `agents/system_prompt.py`).
- **Tool Use:** All data gathering and trading actions must use registered tools (see `tools/`).
- **Order Execution:** Use `OrderRequest` and `send_order` in `metatrader/order_execution.py` for all trades. Always check return values for success/failure.

## Key Conventions & Patterns
- **Risk Management:**
  - Max 1% risk per trade, 5% total concurrent risk.
  - Dynamic position sizing based on account info and stop-loss distance.
- **Data Flow:**
  - Agents use tools to fetch account info, open orders, history, and market data before making decisions.
  - Web search (via Tavily) is used for fundamental/news analysis.
- **Error Handling:**
  - All MT5 actions return structured dicts with `success` and `error` fields. Always check these before proceeding.
- **Extending Tools:**
  - New tools must be registered in `agents/main_agent.py` and follow the LangChain `@tool` pattern.

## Developer Workflows
- **Run the bot:** Activate your Python environment, then run `python main.py`.
- **Dependencies:** See `requirements.txt`. Uses MetaTrader5, LangChain, LangGraph, pandas, and more.
- **Testing:** No formal test suite; validate by running `main.py` and checking order results/logs.
- **Debugging:** Most errors are surfaced via returned dicts from MT5 wrappers. Print or log these for troubleshooting.

## Integration Points
- **MetaTrader 5:** All trading logic routes through `metatrader/` modules.
- **LangChain/LangGraph:** Agent logic and tool orchestration.
- **Tavily Web Search:** For real-time news/fundamental data (see `tools/tavily_web_search.py`).

## Examples
- To place a trade: Use `OrderRequest` and `send_order` as in `main.py`.
- To add a tool: Implement in `tools/`, register in `agents/main_agent.py`, and document usage in the system prompt if needed.

---
For more details, see `agents/system_prompt.py` for agent behavior and `README.md` for a high-level summary.
