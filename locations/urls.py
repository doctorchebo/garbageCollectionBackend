from django.urls import path, include
from .views import LocationsViewSet, UserLocationsViewSet, LocationAddAPIView, LocationListAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all-locations', LocationsViewSet, basename='all_locations')
router.register(r'locations', UserLocationsViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
    path('add-location', LocationAddAPIView.as_view(), name= 'add_location'),
    path('my-locations', LocationListAPIView.as_view(), name= 'my_locations')
]

urlpatterns += router.urls
