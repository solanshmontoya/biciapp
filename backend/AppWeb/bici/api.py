from rest_framework.response import Response
from .models import Store, Location
from .serializers import StoreSerializer, LocationSerializer
from rest_framework import viewsets, permissions

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer    