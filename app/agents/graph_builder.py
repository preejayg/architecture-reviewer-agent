from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from app.agents.nodes import ingest_node, review_node, metadata_node, evaluate_node

# Define what the state looks like (optional but good for clarity)
class State(TypedDict):
    file_path: str
    doc: str
    chunks: List[str]
    review_result: str
    metadata: dict
    error: str

def build_graph():
    """
    Builds the LangGraph stateful agent graph with:
    - Ingest node (token check, chunking)
    - Review node (run review_architecture on each chunk)
    """

    workflow = StateGraph(State)

    # Add nodes
    workflow.add_node("ingest", ingest_node)
    workflow.add_node("metadata", metadata_node)
    workflow.add_node("review", review_node)
    workflow.add_node("evaluate", evaluate_node)

    # Add edges
    workflow.set_entry_point("ingest")
    workflow.add_edge("ingest", "metadata")
    workflow.add_edge("metadata", "review")
    workflow.add_edge("review", "evaluate")
    workflow.add_edge("evaluate", END)

    return workflow.compile()
