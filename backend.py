from tools.search_tool import search_tool
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from typing import TypedDict, List, Annotated
from langgraph.graph import StateGraph,START, END
import operator
from agents import Blog_State,Plan,blog_planner

graph = StateGraph(Blog_State)
graph.add_node("plan",blog_planner)

graph.add_edge(START,"plan")
graph.add_edge("plan",END)

app = graph.compile()

result = app.invoke({"topic":"ethanol in petrol"})
print(result)