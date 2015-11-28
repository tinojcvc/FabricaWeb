
from mongoengine import *

connect('fabricaweb')

class WhatsappReceived(Document):
    phone = StringField(required=True)
    message = StringField(required=False)
    image = StringField(required=True)
    audio = BinaryField(required=False)
    video = BinaryField(required=False)
    is_valid = BooleanField(required=True)
    location = StringField(required=False)
    date_creation = DateTimeField(required=True)
