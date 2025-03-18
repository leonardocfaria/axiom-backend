from notes_features.facade.note import NoteHandler
from notes_features.facade.flashcard import FlashcardHandler
from notes_features.facade.quiz import QuizHandler
from flask_restx import Resource, Namespace
from bson.objectid import ObjectId
from .api_models import note_model

notes_features = Namespace('notes_features', description='Notes related operations')

#Notes
@notes_features.route('/notes/<note_id>')
class Notes(Resource):
    @notes_features.marshal_list_with(note_model)
    def get(self, note_id):
        note_handler = NoteHandler()
        note = note_handler.get_notes_by_field("_id", ObjectId(note_id))

        print(note)
        return note
    
    def delete(self, note_id):
        pass

    def get(self, user_id):
        pass

    def post(self):
        pass

    def put(self):
        pass

#Flashcards
@notes_features.route('/flashcard/')
class Flashcards(Resource):
    def get(self):
        pass

    def post(self, note_id):
        pass

    def delete(self):
        pass

    def put(self):
        pass

#Quizzes
@notes_features.route('/quiz/')
class Quizzes(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass



