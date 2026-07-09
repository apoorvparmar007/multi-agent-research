from tools.search_tool import search_tool
from langchain.agents import create_agent
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# llm = OllamaLLM(model = 'gemma2:2b')

template = """Plan a 500 words blog on a given topic. "
        "Return ONLY valid JSON matching this schema:\n"
        '{\n'
        '  "blog_title": "<string>",\n'
        '  "tasks": [{"id": <int>, "title": "<string>", "brief": "<string>"}]\n'
        '}\n'
        "The blog should have multiple sections. "
        "Do not include any extra text or markdown—only JSON."""

# prompt = PromptTemplate(
#     input_variables=[
#         "topic",
#     ],
#     template=template,
# )

agent = create_agent(model="ollama:qwen3:8b",
    tools=[search_tool],
    system_prompt=template
)

# agent_executor = AgentExecutor(
#     agent=agent, tools=[search_tool], verbose=True, handle_parsing_errors=True
# )

result = agent.invoke({"messages": [{"role": "user", "content": "Ethanol in petrol in India"}]})
print(result)