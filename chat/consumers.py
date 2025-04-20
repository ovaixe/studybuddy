from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from base.models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        # Convert hyphens back to spaces
        self.room_name = room_name.replace("_", " ")
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recieve message from websocket
    async def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message_body = text_data_json['message']
        username = text_data_json['username']
        room_name = text_data_json['room_name']

        # Save message to the database
        room = await self.get_room(room_name)
        user = await self.get_user(username)
        message = await self.save_message(room, user, message_body)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    # Recieve message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to websocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    @sync_to_async(thread_sensitive=True)
    def get_room(self, room_name):
        return Room.objects.get(name=room_name)

    @sync_to_async(thread_sensitive=True)
    def get_user(self, username):
        return User.objects.get(username=username)

    @sync_to_async(thread_sensitive=True)
    def save_message(self, room, user, message):
        return Message.objects.create(room=room, user=user, body=message)
