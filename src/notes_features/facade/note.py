from notes_features.facade.pdf_parser import PDFParser
from notes_features.facade.db import MongoDBHandler
from notes_features.constants.constants import NOTE_COLLECTION
from bson.objectid import ObjectId

class NoteHandler:
    def __init__(self):
        self.db_handler = MongoDBHandler()
        self.col = self.db_handler.db[NOTE_COLLECTION]
        return
    
    def create_note_from_file(self, path, topic, title):
        parser = PDFParser()
        content = parser.parse_pdf(path)
        mydict = { "title": title, "topic": topic, "content": content }
        x = self.col.insert_one(mydict)
        return x.inserted_id
    
    def create_note_from_text(self, text, topic, title):
        mydict = { "title": title, "topic": topic, "content": text }
        x = self.col.insert_one(mydict)
        return x.inserted_id
    
    def get_notes_by_user(self, user_id):
        return self.db_handler.read_many(NOTE_COLLECTION, {"user_id": ObjectId(user_id)})

    def get_notes_by_field(self, field, value):
        return self.db_handler.read_many(NOTE_COLLECTION, {field: value})

    def delete_note(self, note_ids):
        return self.db_handler.delete(NOTE_COLLECTION, {"_id": {"$in": ObjectId(note_ids)}})
    
    def update_note(self, note_id, field, data):
        return self.db_handler.update(NOTE_COLLECTION, {"_id": ObjectId(note_id)}, field, data)
    
