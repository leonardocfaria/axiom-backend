from api import app
from notes_features.facade.note import NoteHandler
from notes_features.facade.flashcard import FlashcardHandler
from notes_features.facade.quiz import QuizHandler
from flask import request

#Notes
@app.route('/notes/<user_id>', methods = ['GET'])
def get_notes_by_user(user_id):
    pass

@app.route('/notes', methods = ['POST'])
def add_notes():
    note_handler = NoteHandler()
    if request.form['type'] == 'file':
        note_handler.create_note_from_file(request.form['path'], request.form['topic'], request.form['title'])
    else:
        note_handler.create_note_from_text(request.form['text'], request.form['topic'], request.form['title'])

@app.route('/notes/<note_id>', methods = ['DELETE'])
def delete_note(note_id):
    pass

#Flashcards
@app.route('/flashcard/<user_id>', methods = ['GET'])
def get_flashcards_by_user(user_id):
    pass

@app.route('/flashcard/<note_id>', methods = ['GET'])
def get_flashcards_by_note_id(note_id):
    pass

@app.route('/flashcard/<note_id>', methods = ['POST'])
def add_flashcard(note_id):
    flashcard_handler = FlashcardHandler()
    flashcard_handler.create_flashcard(note_id)


@app.route('/flashcard/<flashcard_id>', methods = ['DELETE'])
def delete_flashcard(flashcard_id):
    pass

#Quizzes
