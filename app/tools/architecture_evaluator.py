from app.config.settings import settings
from app.llm.llm import call_llm
from app.utils.prompt_loader import render_prompt
from app.utils.logger import get_logger



logger = get_logger("reviewer")

def evaluate_architecture(text: str) -> str:
    """
        Evaluates architecture design text against AWS Well-Architected and other principles.

        Args:
            text (str): Parsed architecture document text.

        Returns:
            str: Evaluation result in Markdown format.
    """

    try:
        logger.info("🔍 Starting architecture review")

        context = {"document_content": text}
        prompt = render_prompt("architecture_evaluator_prompt.txt", context)
        response = call_llm(prompt)

        logger.info("✅ Architecture evaluation completed")

        return response

    except Exception as e:
        logger.error(f"❌ Error during architecture evaluation: {e}")
        return f"❌ Error during architecture evaluation: {e}"
