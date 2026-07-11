from datetime import date

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage
from config import tools, memory, llm_with_tools
from state import State

def build_graph() -> StateGraph:
    graph_builder = StateGraph(State)

    def chatbot(state: State):
        system = SystemMessage(content=(
            f"Today is {date.today().isoformat()}. "
            "For current or recent events, use the search tool and TRUST its "
            "results over your prior knowledge: if the search says something has "
            "already happened, then it has already happened. Do not add the "
            "'time_range' filter unless strictly necessary, since it often "
            "returns empty results. "
            "Base your answer ONLY on facts explicitly stated in the search "
            "results. Distinguish clearly between matches that have already been "
            "played and matches that are scheduled or upcoming. If the results "
            "do not clearly state something, say you don't know instead of "
            "guessing."
        ))
        message = llm_with_tools.invoke([system] + state["messages"])
        return{"messages": [message]}
    
    graph_builder.add_node("chatbot", chatbot)

    tool_node = ToolNode(tools)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_conditional_edges("chatbot", tools_condition)

    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_edge(START, "chatbot")

    return graph_builder.compile(checkpointer=memory)