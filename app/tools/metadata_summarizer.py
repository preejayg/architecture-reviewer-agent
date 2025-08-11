import json
from app.config.settings import settings
from app.llm.llm import call_llm
from app.utils.prompt_loader import render_prompt

def summarize_metadata(doc: str) -> dict:
    context = {"document_content": doc}
    prompt = render_prompt("architecture_summary_prompt.txt", context)

    response = call_llm(prompt)
    
    try:
        # Parse the JSON response
        metadata = json.loads(response)
        return metadata
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return {
            "title": "Architecture Document",
            "summary": response[:200] + "..." if len(response) > 200 else response,
            "topics": ["architecture", "design"]
        }

