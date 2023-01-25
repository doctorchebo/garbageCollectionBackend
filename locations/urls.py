from django.urls import path, include
from .views import LocationViewSet, MyLocationsViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'mylocations', MyLocationsViewSet, basename='mylocations')

urlpatterns = [
    path('', include(router.urls)),
]