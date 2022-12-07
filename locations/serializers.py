from .models import Location
from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
# Serializers define the API representation.
class LocationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='email'
    )
    user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='email'
    )

    class Meta:
        model = Location
        fields = ['id', 'user', 'lat', 'lng', 'cleaning_state', 'created', 'modified']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(LocationSerializer, self).create(validated_data)


class LocationListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='email'
    )
    cleaning_state = serializers.SerializerMethodField()

    user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='email'
    )

    class Meta:
        model = Location
        fields = ['id', 'user', 'lat', 'lng', 'cleaning_state', 'created', 'modified']

    def get_cleaning_state(self, obj):
        return obj.get_cleaning_state_display()
