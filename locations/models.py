from django.db import models
from garbageBackend.settings import AUTH_USER_MODEL
import uuid
class Location(models.Model):  
    CLEAN_STATE = (
        ('NC', "Not Cleaned"),
        ('CL', "Cleaning"),
        ('CD', "Cleaned"),
    )
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, max_length=36) 
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    lat = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    lng = models.DecimalField(max_digits=50, decimal_places=20, blank=True, null=True)
    cleaning_state = models.CharField(max_length=15, blank=True, null=True, choices=CLEAN_STATE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user} {self.lat} {self.lng}'
