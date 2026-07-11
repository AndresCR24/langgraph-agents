from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

memory = MemorySaver()

tavily_tool = TavilySearch(
    max_results=3,
    include_answer=True,
    search_depth="basic",
)
tools = [tavily_tool]

llm = init_chat_model("openai:gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)

graph_config = {"configurable": {"thread_id": 1}}