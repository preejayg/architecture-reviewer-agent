from app.agents.nodes import metadata_node

def test_metadata_node():
    doc = "This document describes a modern SaaS platform architecture built on AWS..."
    state = {"doc": doc}
    result = metadata_node(state)

    assert "metadata" in result
    assert "title" in result["metadata"]
    assert "summary" in result["metadata"]
    assert isinstance(result["metadata"]["topics"], list)
