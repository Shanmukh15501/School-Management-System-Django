

from Masters.models import City
from rest_framework import serializers


class CityMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')
