from metatrader.market_data import candle_data, symbol_info, tradeable_symbols
from langchain.tools import tool


@tool
def get_candel_data_tools(
    symbol: str, timeframe: int, initial_bar_index: int, number_of_bars: int
):
    return candle_data(symbol, timeframe, initial_bar_index, number_of_bars)


@tool
def symbol_info_tool(symbol: str):
    return symbol_info(symbol)


@tool
def tradeable_symbols_tool():
    return tradeable_symbols()
