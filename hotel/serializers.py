from rest_framework import serializers

from clients.serializers import ClientSerializer
from hotel.models import Hotel, Comment


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'stars', 'location']


class CommentSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(required=False)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            # 'client',
            'body',
            'createdAt',
            'updatedAt',
        )

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
