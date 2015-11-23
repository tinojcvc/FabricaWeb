
from mongoengine import *
from FabricaWeb.settings import DBNAME

connect(DBNAME)

class MobileDevice(Document):
    photo = StringField(required=True)
    latitude = DecimalField(required=True)
    longitude = DecimalField(required=True)
    altitude = DecimalField(required=True)
    orientation = DecimalField(required=True)
    speed = FloatField(required=True)
    imei_device = StringField(required=True)
    number_phone = IntField(required=False)
    message = StringField(required=False)
    date_creation = DateTimeField(required=True)

