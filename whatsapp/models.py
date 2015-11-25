
from mongoengine import *
from FabricaWeb.settings import DBNAME

connect(DBNAME)

class WhatsApp(Document):
    phone = IntField(required=True)
    message = StringField(required=False)
    image = StringField(required=False)
    audio = BinaryField(required=False)
    location = StringField(required=False)
    date_creation = DateTimeField(required=True)

