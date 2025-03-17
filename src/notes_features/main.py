from notes_features.facade.flashcard import FlashcardHandler

def main():
    flashcard_handler = FlashcardHandler()
    flashcard = flashcard_handler.create_flashcard("67cafaa0cc1663351789b1c9")
    print(flashcard)