
from mongoengine import *

connect('fabricaweb')

class Account(Document):
    login = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=False)
    is_admin = BooleanField(default=False)

