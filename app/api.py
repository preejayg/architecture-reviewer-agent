from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import tempfile
import uuid
from werkzeug.utils import secure_filename
from app.agents.graph_builder import build_graph
from app.utils.logger import get_logger
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

logger = get_logger("api")

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'md', 'txt'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Architecture Reviewer API is running"})

@app.route('/api/review', methods=['POST'])
def review_architecture():
    """Main endpoint for architecture review"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Unsupported file type. Please upload PDF, MD, or TXT files"}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        logger.info(f"📁 File uploaded: {filename}")
        
        # Process with architecture reviewer
        try:
            graph = build_graph()
            input_state = {"file_path": file_path}
            
            logger.info("🔄 Starting architecture review...")
            result = graph.invoke(input_state)
            
            # Clean up uploaded file
            os.remove(file_path)
            
            if "error" in result:
                logger.error(f"❌ Review failed: {result['error']}")
                return jsonify({
                    "error": result["error"],
                    "status": "failed"
                }), 500
            
            # Prepare response
            response_data = {
                "status": "success",
                "filename": filename,
                "review": result.get("review_result", ""),
                "metadata": result.get("metadata", {}),
                "chunks_processed": len(result.get("chunks", [])),
                "timestamp": result.get("timestamp", "")
            }
            
            logger.info("✅ Architecture review completed successfully")
            return jsonify(response_data)
            
        except Exception as e:
            # Clean up file on error
            if os.path.exists(file_path):
                os.remove(file_path)
            logger.error(f"❌ Error during review: {str(e)}")
            return jsonify({
                "error": f"Review processing failed: {str(e)}",
                "status": "failed"
            }), 500
            
    except Exception as e:
        logger.error(f"❌ API error: {str(e)}")
        return jsonify({
            "error": f"Server error: {str(e)}",
            "status": "failed"
        }), 500

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """Endpoint for user feedback"""
    try:
        data = request.get_json()
        feedback_type = data.get('type')  # 'helpful', 'not_helpful'
        review_id = data.get('review_id')
        comment = data.get('comment', '')
        
        logger.info(f"📝 Feedback received: {feedback_type} for review {review_id}")
        
        # Here you could save feedback to a database
        # For now, just log it
        feedback_data = {
            "type": feedback_type,
            "review_id": review_id,
            "comment": comment,
            "timestamp": str(uuid.uuid4())
        }
        
        # Save feedback to a file (in production, use a database)
        feedback_file = os.path.join(app.config['UPLOAD_FOLDER'], 'feedback.json')
        try:
            with open(feedback_file, 'a') as f:
                f.write(json.dumps(feedback_data) + '\n')
        except Exception as e:
            logger.warning(f"Could not save feedback: {e}")
        
        return jsonify({"status": "success", "message": "Feedback submitted successfully"})
        
    except Exception as e:
        logger.error(f"❌ Feedback error: {str(e)}")
        return jsonify({"error": "Failed to submit feedback"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
