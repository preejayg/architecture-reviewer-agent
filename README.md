# Architecture Reviewer Agent

A sophisticated AI-powered tool that automatically reviews and evaluates software architecture documents against AWS Well-Architected Framework pillars. Built with LangGraph, LangChain, and modern Python technologies.

## 🚀 Features

- **📄 Multi-format Document Support**: Parse PDF, Markdown, and text files
- **🧠 AI-Powered Analysis**: Uses Together AI's Mixtral model for intelligent architecture review
- **📊 AWS Well-Architected Framework**: Scores against Security, Reliability, Performance, Cost, and Operations pillars
- **📝 Metadata Extraction**: Automatically generates document summaries and key topics
- **🔧 Modular Architecture**: Built with LangGraph for flexible workflow management
- **📈 Token Management**: Intelligent document chunking for large files
- **🔄 Stateful Processing**: Maintains context throughout the review process

## 🏗️ Architecture

The project uses a **LangGraph-based workflow** with the following components:

```
📁 app/
├── 🧠 agents/
│   ├── graph_builder.py    # Main workflow orchestration
│   ├── nodes.py           # Processing nodes (ingest, review, metadata)
│   └── tools.py           # Tool wrappers for external services
├── 🔧 config/
│   └── settings.py        # Configuration management
├── 📄 parsers/
│   └── document_parser.py # Document parsing utilities
├── 🛠️ tools/
│   ├── architecture_evaluator.py
│   ├── architecture_reviewer.py
│   └── metadata_summarizer.py
└── 📊 utils/
    ├── llm.py             # LLM client management
    ├── logger.py          # Logging utilities
    └── token_utils.py     # Token counting and chunking
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Together AI API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd architecture-reviewer-agent
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your Together AI API key
   ```

5. **Run the application**
   ```bash
   python -m app.main
   ```

## 📖 Usage

### Command Line Interface

```bash
# Review a document
python -m app.main

# The application will process test_data/sample_doc.md by default
```

### Programmatic Usage

```python
from app.agents.graph_builder import build_graph

# Build the workflow
graph = build_graph()

# Process a document
result = graph.invoke({"file_path": "path/to/your/document.pdf"})

# Access results
print(result["review_result"])  # Architecture review
print(result["metadata"])       # Document metadata
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
TOGETHER_API_KEY=your_together_ai_api_key_here
MODEL_NAME=mistralai/Mixtral-8x7B-Instruct-v0.1
```

### Settings

Key configuration options in `app/config/settings.py`:

- `TOGETHER_API_KEY`: Your Together AI API key
- `MODEL_NAME`: The LLM model to use for analysis
- `MAX_TOKENS`: Maximum tokens per chunk (default: 1500)

## 📊 Output Format

The architecture reviewer provides comprehensive analysis:

### Review Results
- **AWS Well-Architected Pillar Scores** (1-5 scale)
- **Detailed Improvement Suggestions** for each pillar
- **Security Recommendations**
- **Performance Optimization Tips**
- **Cost Optimization Strategies**
- **Operational Excellence Guidelines**

### Metadata
- **Document Title**: Suggested title for the architecture document
- **Summary**: 3-5 sentence summary of the architecture
- **Key Topics**: List of important architectural domains

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_architecture_evaluator.py -v
```

## 🔍 Workflow Details

### 1. Document Ingestion (`ingest_node`)
- Parses uploaded documents (PDF, MD, TXT)
- Extracts clean text content
- Performs token counting
- Splits large documents into manageable chunks

### 2. Metadata Generation (`metadata_node`)
- Analyzes document content
- Generates title suggestions
- Creates document summaries
- Identifies key architectural topics

### 3. Architecture Review (`review_node`)
- Evaluates each document chunk
- Scores against AWS Well-Architected Framework
- Provides detailed improvement recommendations
- Aggregates results from multiple chunks

## 🛠️ Development

### Project Structure

```
architecture-reviewer-agent/
├── 📁 app/                    # Main application code
│   ├── 🧠 agents/            # LangGraph agents and nodes
│   ├── 🔧 config/            # Configuration management
│   ├── 📄 parsers/           # Document parsing utilities
│   ├── 🛠️ tools/             # External service integrations
│   └── 📊 utils/             # Utility functions
├── 📁 tests/                 # Test suite
├── 📁 test_data/             # Sample documents for testing
├── 📁 uploads/               # Temporary file storage
├── 📄 requirements.txt       # Python dependencies
├── 📄 .env.example          # Environment variables template
└── 📄 README.md             # This file
```

### Adding New Features

1. **New Document Parser**: Add to `app/parsers/`
2. **New Analysis Tool**: Add to `app/tools/`
3. **New Workflow Node**: Add to `app/agents/nodes.py`
4. **Configuration**: Update `app/config/settings.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Together AI** for providing the LLM infrastructure
- **LangGraph** for the workflow orchestration framework
- **AWS** for the Well-Architected Framework
- **PyMuPDF** for PDF parsing capabilities

## 📞 Support

For questions, issues, or contributions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include error logs and sample documents when applicable

---

**Built with ❤️ using LangGraph, LangChain, and modern Python technologies**
