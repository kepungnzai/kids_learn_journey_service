from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from datetime import datetime

class Course(Document):
    title = StringField(required=True)
    description = StringField()
    students = ListField(ReferenceField('User'))
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    user_type = StringField(choices=['student', 'teacher', 'admin'], required=True)
    courses = ListField(ReferenceField(Course))
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)