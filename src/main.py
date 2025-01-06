# Main entry point for CaptchaXtract standalone application

from flask import Flask, request, jsonify
from config import Config
from image_to_text_libs import ImageToTextAdmin

app = Flask(__name__)
config = Config()
image_to_text_admin = ImageToTextAdmin()

@app.route('/submit-task', methods=['POST'])
def submit_task():
    api_key = request.headers.get('API-Key')
    if not api_key:
        return jsonify({"error": "API-Key header is required"}), 400

    if api_key not in config.API_KEYS:
        return jsonify({"error": "Invalid API-Key"}), 403

    image_file = request.files.get('file')
    if not image_file:
        return jsonify({"error": "Image file is required"}), 400

    result = image_to_text_admin.image_to_text(image_file)
    return jsonify(result)

@app.route('/get-result', methods=['GET'])
def get_result():
    api_key = request.headers.get('API-Key')
    if not api_key:
        return jsonify({"error": "API-Key header is required"}), 400

    if api_key not in config.API_KEYS:
        return jsonify({"error": "Invalid API-Key"}), 403

    task_id = request.args.get('task_id')
    if not task_id:
        return jsonify({"error": "Task ID is required"}), 400

    # Simulate a stored result
    result = {"task_id": task_id, "result": "Sample extracted text"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.API_PORT)
