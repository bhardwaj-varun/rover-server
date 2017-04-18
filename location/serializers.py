from rest_framework import serializers
from location.models import Location

class LocationSerializer(serializers.ModelSerializer):

    dateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude', 'accuracy', 'dateTime')