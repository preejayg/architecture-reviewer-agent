from app.tools.architecture_reviewer import review_architecture as review_architecture_tool
from app.tools.architecture_evaluator import evaluate_architecture as evaluate_architecture_tool
from app.tools.metadata_summarizer import summarize_metadata

def generate_metadata(doc: str) -> dict:
    """Extracts metadata like title, summary, keywords from document."""
    return summarize_metadata(doc)


def review_architecture(doc: str) -> str:
    """Tool that reviews architecture document content."""
    return review_architecture_tool(doc)


def evaluate_architecture(doc: str) -> str:
    """Tool that evaluates architecture document content."""
    return evaluate_architecture_tool(doc)

