from django.shortcuts import render
from rest_framework import viewsets
from users.models import CustomUser
from .serializers import LocationSerializer, LocationListSerializer
from .models import Location
from rest_framework.decorators import action
# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset
         
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LocationSerializer
        elif self.request.method == 'GET':
            return LocationListSerializer
        
        