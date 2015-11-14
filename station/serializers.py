
from rest_framework import serializers
from station.models import Station, StationValues

class StationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    num_station = serializers.IntegerField()
    date_creation = serializers.DateTimeField()

    def create(self, validated_data):
        return Station.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.num_station = validated_data.get('num_station', instance.num_station)
        instance.date_creation = validated_data.get('date_creation', instance.date_creation)
        instance.save()
        return instance

class StationValuesSerializer(serializers.Serializer):
    station = serializers.CharField(read_only=True)
    pressure = serializers.FloatField()
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()

    def create(self, validated_data):
        return StationValues.objects.create(**validated_data)

