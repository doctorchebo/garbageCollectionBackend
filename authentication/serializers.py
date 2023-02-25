from users.models import CustomUser
from rest_framework import serializers
class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15)

    def create(self, validated_data):
        email = self.validated_data['email']
        password = validated_data.pop('password')
        user = CustomUser.objects.create(username=email, **validated_data)
        user.set_password(password)
        user.save()
        return user


