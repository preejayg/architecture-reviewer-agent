import os
import fitz  # PyMuPDF
from markdown_it import MarkdownIt
from app.utils.logger import get_logger

logger = get_logger("parser")

def parse_pdf(file_path: str) -> str:
    """Extracts and cleans text from a PDF file."""
    text_content = []
    try:
        with fitz.open(file_path) as pdf_doc:
            for page_num, page in enumerate(pdf_doc, start=1):
                text = page.get_text("text")
                if text:
                    text_content.append(text.strip())
                else:
                    logger.warning(f"⚠️ No text found on page {page_num}")
        return "\n\n".join(text_content).strip()
    except Exception as e:
        logger.error(f"❌ PDF parsing failed: {e}")
        return ""

def parse_markdown(file_path: str) -> str:
    """Reads and converts markdown into plain text."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        md = MarkdownIt()
        parsed_tokens = md.parse(md_content)
        plain_text = []
        for token in parsed_tokens:
            if token.type == "inline":
                plain_text.append(token.content.strip())
        return "\n".join(plain_text).strip()
    except Exception as e:
        logger.error(f"❌ Markdown parsing failed: {e}")
        return ""

def parse_document(file_path: str) -> str:
    """
    Detect file type and parse accordingly.
    Supports: PDF (.pdf) and Markdown (.md)
    """
    if not os.path.exists(file_path):
        logger.error(f"❌ File not found: {file_path}")
        return ""

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        logger.info(f"📄 Parsing PDF: {file_path}")
        return parse_pdf(file_path)

    elif ext == ".md":
        logger.info(f"📝 Parsing Markdown: {file_path}")
        return parse_markdown(file_path)

    else:
        logger.error(f"❌ Unsupported file type: {ext}")
        return ""
