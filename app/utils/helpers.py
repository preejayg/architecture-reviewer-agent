import logging
from typing import List
from tiktoken import get_encoding

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def split_text_by_tokens(text: str, max_tokens: int = 2048, encoding_name: str = "cl100k_base") -> List[str]:
    encoding = get_encoding(encoding_name)
    tokens = encoding.encode(text)
    
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [encoding.decode(chunk) for chunk in chunks]
