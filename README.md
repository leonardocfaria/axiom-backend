# axiom-backend

Flask REST API backend for the Axiom application — a note management system with AI-powered features including flashcard generation and quizzes.

## Features

- Notes CRUD via REST API (Flask-RESTX)
- Flashcard generation from notes
- Quiz generation from notes
- AI integration via Google Gemini
- Document ingestion with Docling
- MongoDB for persistence

## Tech Stack

- Python 3.12
- Flask + Flask-RESTX
- MongoDB + PyMongo
- Google GenAI SDK
- Docling
- PDM (package manager)

## Getting Started

### Prerequisites

- Python 3.12
- MongoDB running locally or via URI
- PDM installed (`pip install pdm`)

### Install

```bash
pdm install
```

### Run

```bash
# Start the API server
pdm run api

# Run the notes processing features
pdm run notes_features
```

## Project Structure

```
src/
├── api/            # Flask-RESTX routes and models
└── notes_features/ # AI-powered note processing (flashcards, quizzes)
```
