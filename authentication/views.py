from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
import jwt
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from users.models import CustomUser
from .utils import Util
from .serializers import CustomUserSerializer
from garbageBackend import settings


class CreateUserViewSet(generics.GenericAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] 
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
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
    authentication_classes = [] #disables authentication
    permission_classes = [] 
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            print('payload 1 ' + str(payload))
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

