from django.contrib.auth.models import User, Group
from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'address', 'phone']