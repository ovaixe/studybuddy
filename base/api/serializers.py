from rest_framework.serializers import ModelSerializer
from base.models import Room, Topic, Message


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


    def create(self, validated_data):
        topic, created = Topic.objects.get_or_create(name=validated_data['name'])
        return topic


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
