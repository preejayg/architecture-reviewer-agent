from app.llm.llm_factory import get_llm_client
from app.config.settings import settings
from app.utils.logger import get_logger

logger = get_logger("llm")
client = get_llm_client()

def call_llm(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    """
    Call LLM using the Together client from the factory.
    """
    try:
        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.4
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"❌ LLM call failed: {e}")
        return f"Error calling LLM: {e}"
