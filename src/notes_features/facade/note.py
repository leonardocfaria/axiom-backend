from pdf_parser import PDFParser
from db import MongoDBHandler
from notes_features.constants.constants import NOTE_COLLECTION

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
        