from app.models import Coordinates
from django.contrib import admin


class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'lat', 'lng', 'created')


admin.site.register(Coordinates, CoordinatesAdmin)
