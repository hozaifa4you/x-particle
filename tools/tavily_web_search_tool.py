from langchain.tools import tool
from config.tavily import tavily


@tool
def tavily_web_search_tool(query: str) -> dict:
    """
    Search market data, news, and other relevant information for Forex trading using Tavily.

    Args:
        query (str): The search query string.

    Returns:
        5 dict of search result.
    """

    result = tavily.search(query=query, max_results=5)
    return result
