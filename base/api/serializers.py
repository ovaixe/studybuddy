from rest_framework.serializers import ModelSerializer
from base.models import Room, Topic, Message


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'topic', 'host', 'description']


    # def create(self, validated_data):
    #     # validated_data['host'] = self.context['request'].user
    #     print(validated_data)
    #     validated_data['topic'] = Topic.objects.get(name=validated_data['topic'])
    #     return Room.objects.create(**validated_data)


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
