from langchain.tools import tool
from config.tavily import tavily


@tool
def google_search(city: str) -> dict:
    """
    Search current weather for a city using Tavily.
    """

    query = f"Current weather in city {city}"
    result = tavily.search(query=query, max_results=2)
    return result
