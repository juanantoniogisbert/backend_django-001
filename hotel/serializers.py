from rest_framework import serializers

from clients.serializers import ClientSerializer
from hotel.models import Hotel, Comment


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'stars', 'location']


class CommentSerializer(serializers.ModelSerializer):
    # clients = ClientSerializer(required=True)
    # hotels = HotelSerializer(many=True, read_only=True)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'hotels',
            'clients',
            'body',
            'createdAt',
            'updatedAt'
        )

        depth = 1
        extra_kwargs = {'body':{'read_only': True}}

    def create(self, validated_data):
        hotel = self.context['hotel']
        # client = self.context['client']

        return Comment.objects.create(
            hotel=hotel, **validated_data
            # hotel=hotel, **validated_data
        )


    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
