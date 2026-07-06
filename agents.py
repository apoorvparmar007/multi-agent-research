from tools.search_tool import search_tool
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from typing import TypedDict, List, Annotated
from langgraph.graph import StateGraph,START, END
import operator
from langchain_ollama import OllamaLLM
from langgraph.prebuilt import create_react_agent

llm = OllamaLLM(model = 'gemma2:2b')

class Task(BaseModel):
    id: int
    title: str
    brief: str = Field(..., description="What to cover")

class Plan(BaseModel):
    blog_title: str
    tasks: List[Task]

class Blog_State(TypedDict):
    topic: str
    plan: Plan

    
def blog_planner(state: Blog_State) -> dict:
    topic = state['topic']
    prompt = f"""Plan a 500 words blog on {topic}.
Return ONLY valid JSON matching this schema:
{{
  "blog_title": "<string>",
  "tasks": [{{"id": <int>, "title": "<string>", "brief": "<string>"}}]
}}
The blog should have multiple sections including current view, future outlook, investment opportunities etc.
Do not include any extra text or markdown—only JSON."""

    chain = llm | JsonOutputParser(pydantic_object=Plan)
    plan = chain.invoke(prompt)

    return {"plan":plan}