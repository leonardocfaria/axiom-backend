from notes_features.facade.db import MongoDBHandler
from notes_features.constants.constants import FLASHCARD_COLLECTION
from notes_features.utils.config import config
from google import genai
from json import loads
from bson.objectid import ObjectId

class FlashcardHandler:
    def __init__(self):
        self.db_handler = MongoDBHandler()
        self.col = self.db_handler.db[FLASHCARD_COLLECTION]
        self.genai_client = genai.Client(api_key=config.credentials.gemini_api_key)
        return
    
    def create_flashcard(self, note_id):
        note = self.db_handler.read_one("notes", {"_id": ObjectId(note_id)})

        response = self.genai_client.models.generate_content(
            model="gemini-2.0-flash",
            config={'response_mime_type': 'application/json'},
            contents=f"Generate a flashcard set to help students fixate their knowledge on the following notes with concise flashcards: {note['content']}. The flashcards should be in JSON format with the following structure:\n{{\n  \"title\": \"{note['title']}\",\n  \"flashcards\": [\n    {{\"front\": \"Question 1 text\", \"back\": \"Explanation for question 1\"}},\n    {{\"front\": \"Question 2 text\", \"back\": \"Explanation for question 2\"}},\n    {{\"front\": \"Question 3 text\", \"back\": \"Explanation for question 3\"}}\n  ]\n}}"
        )
        flashcard_set = response.text
        flashcard_set = loads(flashcard_set)
        flashcard_set.update({'note_id': note['_id']})
        x = self.db_handler.create(FLASHCARD_COLLECTION, flashcard_set)

        return x
    
    def delete_flashcard(self, flashcard_id):
        return self.db_handler.delete(FLASHCARD_COLLECTION, {"_id": ObjectId(flashcard_id)})
    
    def get_flashcards_by_user(self, user_id):
        return self.db_handler.read_many(FLASHCARD_COLLECTION, {"user_id": ObjectId(user_id)})
    
    def get_flashcards_by_field(self, field, value):
        return self.db_handler.read_many(FLASHCARD_COLLECTION, {field: value})
    
    def update_flashcard(self, flashcard_id, field, data):
        return self.db_handler.update(FLASHCARD_COLLECTION, {"_id": ObjectId(flashcard_id)}, field, data)
    