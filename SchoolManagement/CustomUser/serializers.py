
from rest_framework import serializers
from rest_framework import generics, status, permissions

from django.contrib.auth import get_user_model

from Masters.serializers import CityMiniSerializer
User = get_user_model()


class UserCommonSerializer(serializers.ModelSerializer):

    city= CityMiniSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['email','phone','role','city']
