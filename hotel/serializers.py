from rest_framework import serializers

from hotel.models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'stars', 'location']
