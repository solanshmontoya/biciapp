
from rest_framework import exceptions, serializers

from datetime import datetime, timedelta, date
from .models import Store, Location, Route

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Location
	    fields = ('latitude', 'longitude',)

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('__all__')