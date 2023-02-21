from users.models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15)
    def save (self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        CustomUser.objects.create(email=email, password=password, username=email)

