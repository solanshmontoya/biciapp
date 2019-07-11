from rest_framework.response import Response
from .models import Store, Location, Route
from .serializers import StoreSerializer, LocationSerializer, RouteSerializer
from rest_framework import viewsets, permissions

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer    

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer