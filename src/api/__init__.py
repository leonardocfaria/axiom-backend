from flask import Flask
from .notes import notes_features
from .extensions import api


app = Flask(__name__)

api.init_app(app)

api.add_namespace(notes_features)


