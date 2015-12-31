
from mongoengine import *
from FabricaWeb.settings import DBNAME

connect(DBNAME)

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    email = StringField(required=False, unique=True)
    last_login = DateTimeField(required=False)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
    date_joined = DateTimeField(required=True)

