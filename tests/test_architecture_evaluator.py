import pytest
from app.evaluators.architecture_evaluator import evaluate_architecture

def test_architecture_eval_with_fixture(sample_doc_text):
    from app.evaluators.architecture_evaluator import evaluate_architecture
    result = evaluate_architecture(sample_doc_text)
    assert isinstance(result, str)
    assert len(result) > 100  # Should return substantial content
    # Check for common evaluation terms that should be in the response
    assert any(term in result.lower() for term in ["security", "reliability", "performance", "cost", "operations"])
