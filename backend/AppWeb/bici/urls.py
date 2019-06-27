
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views, api

router = DefaultRouter()
router.register(r'stores', api.StoreViewSet, 'stores')
router.register(r'locations', api.LocationViewSet, 'locations')

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^', include(router.urls)),
]
