from flask import Blueprint, request, jsonify
import os

dc_blueprint = Blueprint('document_chat', __name__)

@dc_blueprint.route('/documents', methods=['GET'])
def get_documents():
    files = os.listdir('uploads')
    documents = [{'id': i, 'fileName': f} for i, f in enumerate(files)]
    return jsonify(documents)

@dc_blueprint.route('/upload', methods=['POST'])
def upload_document():
    if 'document' not in request.files:
        return "No file part", 400
    file = request.files['document']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        return jsonify({'id': len(os.listdir('uploads')) - 1, 'fileName': file.filename})

@dc_blueprint.route('/chat/<int:doc_id>', methods=['GET'])
def get_chat_history(doc_id):
    # Placeholder: Assuming chat history is stored somewhere
    chat_history = [{"question": "Sample question", "answer": "LG"}]
    return jsonify(chat_history)

@dc_blueprint.route('/chat', methods=['POST'])
def ask_question():
    data = request.json
    doc_id = data['docId']
    question = data['question']
    # Placeholder for Langraph processing
    answer = "LG"
    return jsonify({'question': question, 'answer': answer})