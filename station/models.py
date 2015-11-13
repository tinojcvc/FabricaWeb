
from mongoengine import *
from FabricaWeb.settings import DBNAME

connect(DBNAME)

class Station(Document):
    name = StringField(required=True, unique=True)
    num_station = IntField(required=True, unique=True)
    date_creation = DateTimeField(required=True)

class StationValues(Document):
    station = ReferenceField(Station, required=True)
    pressure = FloatField(required=True)
    temperature = FloatField(required=True)
    humidity = FloatField(required=True)
    wind_speed = FloatField(required=True)
    time = DateTimeField(required=True)

