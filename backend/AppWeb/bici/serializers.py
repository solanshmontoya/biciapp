
from rest_framework import exceptions, serializers

from datetime import datetime, timedelta, date
from .models import Store, Location

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('description', 'address',)

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Location
	    fields = ('latitude', 'longitude',)