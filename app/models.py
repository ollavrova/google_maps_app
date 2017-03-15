from __future__ import unicode_literals
from django.db import models


class Coordinates(models.Model):
    address = models.CharField(max_length=250)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
