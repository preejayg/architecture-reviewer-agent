from app.utils.token_utils import chunk_text

def test_chunk_text():
    text = "This is a long test document. " * 100
    chunks = chunk_text(text, max_tokens=50)
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert len(chunks) > 1
