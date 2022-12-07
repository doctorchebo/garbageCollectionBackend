from django.shortcuts import render
from django.contrib import admin

from users.models import CustomUser
from .serializers import UserSerializer
from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
