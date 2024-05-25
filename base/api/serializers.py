from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        # fields = ['id', 'host', 'topic', 'description']
        fields = '__all__'