import pytest
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture
def sample_doc_path():
    return Path("test_data/sample_doc.md")

@pytest.fixture
def sample_doc_text(sample_doc_path):
    return sample_doc_path.read_text()
