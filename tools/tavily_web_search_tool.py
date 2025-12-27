from langchain.tools import tool
from config.tavily import tavily


@tool
def tavily_web_search_tool(query: str) -> dict:
    """
    Perform a web search using the Tavily API and return summarized results.

    Args:
        query (str): The search query string.

    Returns:
        dict: Search results including titles, links, and snippets for up to 5 results.
    Example:
        {
            'results': [
                {'title': 'EURUSD News', 'link': 'https://...', 'snippet': 'Latest EURUSD market news...'},
                ...
            ]
        }
    """
    result = tavily.search(query=query, max_results=5)
    return result
