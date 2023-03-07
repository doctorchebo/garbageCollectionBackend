from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from users.models import CustomUser
from .serializers import LocationListSerializer, LocationAddSerializer, LocationUpdateSerializer
from .models import Location
from rest_framework.decorators import action
# Create your views here.
class LocationsViewSet(ModelViewSet):
    @action(detail=False)
    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset
    def get_serializer_class(self):
        return LocationListSerializer
    @action(detail=True)
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return LocationUpdateSerializer
        if self.request.method == 'POST':
            return LocationAddSerializer
        else:
            return LocationListSerializer

class UserLocationsViewSet(ModelViewSet):
    @action(detail=False)
    def get_queryset(self):
        queryset = Location.objects.filter(user=self.request.user)
        return queryset
    @action(detail=True)
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return LocationUpdateSerializer
        if self.request.method == 'POST':
            return LocationAddSerializer
        else:
            return LocationListSerializer
class LocationAddViewSet(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationAddSerializer

class LocationUpdateViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    def get_queryset(self):
        queryset = Location.objects.filter(id=self.kwargs['pk'])
        return queryset
    def get_serializer_class(self):
        return LocationUpdateSerializer