from django.contrib import admin

from .models import Store, Location, Route

admin.site.register(Store)
admin.site.register(Location)
admin.site.register(Route)
