import os
from app.agents.graph_builder import build_graph

if __name__ == "__main__":
    # Update this path to match your directory structure
    file_path = os.path.join("test_data", "sample_doc.md")

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        exit(1)

    input_state = {"file_path": file_path}

    graph = build_graph()
    result = graph.invoke(input_state)

    if "error" in result:
        print("⚠️ Review failed:", result["error"])
    else:
        print("✅ Review Complete:\n")
        print(result["review_result"])
        if "metadata" in result:
            print("\n📊 Metadata:")
            print(result["metadata"])
