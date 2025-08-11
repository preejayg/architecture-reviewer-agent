import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback for models not directly supported by tiktoken
        # Use cl100k_base encoding which is commonly used for many models
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def chunk_text(text: str, max_tokens: int = 1000) -> List[str]:
    # Ensure overlap is smaller than chunk size
    overlap = min(100, max_tokens // 4)  # Use 25% of chunk size or 100, whichever is smaller
    
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=max_tokens,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)
