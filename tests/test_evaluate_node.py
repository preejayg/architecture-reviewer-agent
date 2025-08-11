from app.agents.evaluator_node import evaluate_node

def test_evaluate_node():
    state = { "document": "Simple architecture description." }
    new_state = evaluate_node(state)
    assert "evaluation" in new_state
    assert "Error" not in new_state["evaluation"]
