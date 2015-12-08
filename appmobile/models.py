
from mongoengine import *
from FabricaWeb.settings import DBNAME

connect(DBNAME)

class MobileDevice(Document):
    photo = StringField(required=True)
    latitude = DecimalField(required=False)
    longitude = DecimalField(required=False)
    altitude = DecimalField(required=False)
    orientation = DecimalField(required=False)
    speed = StringField(required=False)
    imei_device = StringField(required=False)
    number_phone = IntField(required=False, null=True)
    message = StringField(required=False)
    date_creation = DateTimeField(required=True)
    fire_percentage = DecimalField(required=False)
    is_read = BooleanField(required=True, default=False)
    is_valid = BooleanField(required=True, default=False)

