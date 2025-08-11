from app.agents.tools import review_architecture, evaluate_architecture, generate_metadata
from app.parsers.document_parser import parse_document

from app.utils.logger import get_logger
from app.utils.token_utils import count_tokens, chunk_text
from app.config.settings import settings

logger = get_logger("AgentNodes")

MAX_TOKENS = 1500
MODEL_NAME = settings.MODEL_NAME

def ingest_node(state: dict) -> dict:
    """
    Ingests and preprocesses the input document using the document parser.
    Splits document into chunks if token count exceeds MAX_TOKENS.
    """
    try:
        file_path = state.get("file_path", "")
        if not file_path:
            raise ValueError("No file path found in state.")

        logger.info(f"📄 Parsing document: {file_path}")
        
        # Use document parser to extract text
        doc = parse_document(file_path)
        
        if not doc:
            raise ValueError("Document parser returned empty content.")

        token_count = count_tokens(doc, MODEL_NAME)
        logger.info(f"📄 Ingesting document ({token_count} tokens)")

        if token_count > MAX_TOKENS:
            logger.warning(f"⚠️ Document exceeds {MAX_TOKENS} tokens — chunking required")
            chunks = chunk_text(doc, MAX_TOKENS, MODEL_NAME)
            logger.info(f"📦 Document split into {len(chunks)} chunks")
        else:
            chunks = [doc]
            logger.info("✅ Document within token limit — no chunking")

        return {**state, "doc": doc, "chunks": chunks}

    except Exception as e:
        logger.exception("❌ Error during ingest_node")
        return {**state, "error": f"Error in ingest_node: {str(e)}"}

def review_node(state: dict) -> dict:
    """
    Reviews each chunk using the review_architecture tool.
    Returns the aggregated review.
    """
    try:
        if "error" in state:
            logger.warning("⛔ Skipping review_node due to upstream error")
            return state

        chunks = state.get("chunks", [])
        if not chunks:
            raise ValueError("No chunks found for review.")

        all_reviews = []

        for idx, chunk in enumerate(chunks):
            try:
                logger.info(f"🔍 Reviewing chunk {idx + 1}/{len(chunks)}")
                review = review_architecture(chunk)
                all_reviews.append(f"🧩 Chunk {idx+1} Review:\n{review}")
            except Exception as chunk_err:
                logger.error(f"❌ Error reviewing chunk {idx + 1}: {chunk_err}")
                all_reviews.append(f"❌ Error reviewing chunk {idx + 1}: {chunk_err}")

        combined_review = "\n\n".join(all_reviews)
        logger.info("✅ All chunks reviewed")

        return {**state, "review_result": combined_review}

    except Exception as e:
        logger.exception("❌ Error during review_node")
        return {**state, "error": f"Error in review_node: {str(e)}"}

def evaluate_node(state: dict) -> dict:
    """
    Evaluates each chunk using the evaluate_architecture tool.
    Returns the aggregated evaluation.
    """
    try:
        if "error" in state:
            logger.warning("⛔ Skipping evaluate_node due to upstream error")
            return state

        chunks = state.get("chunks", [])
        if not chunks:
            raise ValueError("No chunks found for evaluation.")

        all_evaluations = []

        for idx, chunk in enumerate(chunks):
            try:
                logger.info(f"🔍 Evaluating chunk {idx + 1}/{len(chunks)}")
                evaluation = evaluate_architecture(chunk)
                all_evaluations.append(f"🧩 Chunk {idx+1} Evaluation:\n{evaluation}")
            except Exception as chunk_err:
                logger.error(f"❌ Error evaluating chunk {idx + 1}: {chunk_err}")
                all_evaluations.append(f"❌ Error evaluating chunk {idx + 1}: {chunk_err}")

        combined_evaluation = "\n\n".join(all_evaluations)
        logger.info("✅ All chunks evaluated")

        return {**state, "evaluation_result": combined_evaluation}

    except Exception as e:
        logger.exception("❌ Error during evaluate_node")
        return {**state, "error": f"Error in evaluate_node: {str(e)}"}

def metadata_node(state):
    try:
        doc = state.get("doc", "")
        if not doc:
            raise ValueError("Document is empty or missing")

        logger.info("🧠 Generating metadata and summary...")


        metadata = generate_metadata(doc)

        logger.info("✅ Metadata generated")
        return {**state, "metadata": metadata}

    except Exception as e:
        logger.error(f"❌ Error in metadata_node: {e}")
        return {"error": str(e)}
