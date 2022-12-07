from django.urls import path, include
from .views import LocationViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
]