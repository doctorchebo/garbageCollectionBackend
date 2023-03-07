from django.urls import path, include
from .views import LocationsViewSet, UserLocationsViewSet, LocationAddViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all-locations', LocationsViewSet, basename='all_locations')
router.register(r'locations', UserLocationsViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
    path('add-location', LocationAddViewSet.as_view(), name= 'add_location')
]

urlpatterns += router.urls
