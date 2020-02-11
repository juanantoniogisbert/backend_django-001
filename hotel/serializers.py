from rest_framework import serializers

from clients.serializers import ClientSerializer
from hotel.models import Hotel, Comment
from profiles.serializers import ProfileSerializer, ProfileSerializerMini


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'stars', 'location']


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializerMini(read_only=True)
    hotels = HotelSerializer(many=False, read_only=True)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'hotels',
            'profile',
            'body',
            'createdAt',
            'updatedAt'
        )

        # depth = 2
        extra_kwargs = {'body':{'read_only': True}}

    def create(self, validated_data):
        hotels = self.context['hotels']
        profile = self.context['profile']

        return Comment.objects.create(
            hotels=hotels, **validated_data,
            profile=profile, **validated_data
        )


    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
