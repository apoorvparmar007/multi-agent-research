from langchain_community.tools import DuckDuckGoSearchResults


def search_tool(query):
    """Search DuckDuckGo for the given query and return results."""
    tool = DuckDuckGoSearchResults()
    response = tool.invoke(query)
    return response