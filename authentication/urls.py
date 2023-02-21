from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomUserViewSet, VerifyEmailView
from django.urls import path, include

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', CustomUserViewSet.as_view({"post": "create"}), name='signup'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]