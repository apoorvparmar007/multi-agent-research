from langchain_community.tools import DuckDuckGoSearchResults


def search_tool(query):
    tool = DuckDuckGoSearchResults()
    response = tool.invoke(query)
    return response