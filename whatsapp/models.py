
from mongoengine import *

connect('fabricaweb')

class WhatsappReceived(Document):
    phone = StringField(required=True)
    message = StringField(required=False)
    image = BinaryField(required=False, null=True)
    audio = BinaryField(required=False, null=True)
    video = BinaryField(required=False, null=True)
    is_valid = BooleanField(required=True, default=False)
    is_complete = BooleanField(required=True, default=False)
    is_read = BooleanField(required=True, default=False)
    location = StringField(required=False)
    date_creation = DateTimeField(required=True)
