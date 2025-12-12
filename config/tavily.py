from tavily import TavilyClient

from config.environments import config

tavily = TavilyClient(api_key=config.TAVILY_API_KEY)
