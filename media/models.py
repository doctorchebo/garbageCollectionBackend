from django.db import models
from locations.models import Location

class Photo(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length = 200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

