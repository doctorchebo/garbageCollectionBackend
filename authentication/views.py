from rest_framework import viewsets
from .serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class CreateUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [] #disables authentication
    permission_classes = [] 
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = CustomUser.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse("verify-email")
            absolute_url= "http://"+current_site+relative_link+"?token="+str(token)
            email_body = "Hi " + user.email + ". Please verify your email clicking on the following link: \n" + absolute_url 
            data = {"email_body": email_body, "email_to": user.email, "subject": "Please verify your email"}
            Util.send_email(data)
            return Response(user_data, status=status.HTTP_201_CREATED)
class VerifyEmailView(generics.GenericAPIView):
    def get(self):
        pass
