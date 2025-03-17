from google import genai
from notes_features.constants.constants import QUIZ_COLLECTION
from db import MongoDBHandler
from notes_features.utils.config import config
from json import loads
from bson.objectid import ObjectId


class QuizHandler:
    def __init__(self):
        self.db_handler = MongoDBHandler()
        self.col = self.db_handler.db[QUIZ_COLLECTION]
        self.genai_client = genai.Client(api_key=config.credentials.gemini_api_key)
        return
    
    def create_quiz(self, note_id):
        note = self.db_handler.read_one("notes", {"_id": ObjectId(note_id)})

        response = self.genai_client.models.generate_content(
            model="gemini-2.0-flash",
            config= {'response_mime_type':'application/json'},
            contents=f"Generate a multiple-choice quiz to test the student's knowledge on the following notes: {note['content']}. The quiz should be in JSON format with the following structure:\n{{\n  \"title\": \"{note['title']}\",\n  \"questions\": [\n    {{\"question_number\": 1, \"question\": \"What is the main topic discussed in the notes?\", \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"], \"correct_option\": 1}},\n    {{\"question_number\": 2, \"question\": \"What is the key concept explained in the notes?\", \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"], \"correct_option\": 2}},\n    {{\"question_number\": 3, \"question\": \"Provide an example mentioned in the notes.\", \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"], \"correct_option\": 3}}\n  ]\n}}"
        )
        quiz = response.text
        quiz = loads(quiz)
        quiz.update({'note_id': note['_id']})

        return quiz

    def explain_question(self, question, answer):
        response = self.genai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Explain why the answer the question: {question} is {answer}."
        )

        explanation = response.text

        return explanation