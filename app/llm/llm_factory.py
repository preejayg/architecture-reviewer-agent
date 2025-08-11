from together import Together
from app.config.settings import settings
from app.utils.logger import get_logger

logger = get_logger("llm_factory")

def get_llm_client() -> Together:
    """
    Factory to create and return a Together client.
    """
    try:
        return Together(api_key=settings.TOGETHER_API_KEY)
    except Exception as e:
        logger.error(f"❌ Failed to initialize Together client: {e}")
        raise
