from mongoengine import Document
from mongoengine.fields import BooleanField, EmailField, StringField


class Contact(Document):
    name = StringField()
    email = EmailField()
    isSent = BooleanField(default=False)
