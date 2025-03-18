from flask_restx import fields
from .extensions import api

note_model = api.model('Note', {
    'id': fields.Integer(required=True, description='The note unique identifier'),
    'title': fields.String(required=True, description='The note title'),
    'topic': fields.String(required=False, description='The note topic'),
    'content': fields.String(required=True, description='The note content')
})