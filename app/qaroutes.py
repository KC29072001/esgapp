# backend/app/qaroutes.py
from flask import Blueprint, request, jsonify
from .models import db, Questionnaire, Question

qa_blueprint = Blueprint('qa', __name__)

@qa_blueprint.route('/create', methods=['POST'])
def create_questionnaire():
    data = request.get_json()
    name = data.get('name')
    questions = data.get('questions')

    if not name or not questions:
        return jsonify({"error": "Name and questions are required"}), 400

    questionnaire = Questionnaire(name=name)
    db.session.add(questionnaire)
    db.session.commit()

    for question_text in questions:
        question = Question(text=question_text, questionnaire_id=questionnaire.id)
        db.session.add(question)
    db.session.commit()

    return jsonify({"message": "Questionnaire created successfully"}), 201

@qa_blueprint.route('/list', methods=['GET'])
def list_questionnaires():
    questionnaires = Questionnaire.query.all()
    result = []
    for questionnaire in questionnaires:
        questions = [q.text for q in questionnaire.questions]
        result.append({"id": questionnaire.id, "name": questionnaire.name, "questions": questions})
    return jsonify(result), 200
