from app.models import Coordinates
from rest_framework import serializers


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ('id', 'address', 'lat', 'lng', 'created')

    def create(self, validated_data):
        """
        Create and return a new `Coordinates` instance, given the
        validated data.
        """
        return Coordinates.objects.create(**validated_data)
