from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.db.models import Q
from base.models import Room, Topic, Message
from .serializers import RoomSerializer, TopicSerializer, MessageSerializer


@api_view(['GET'])
def getRoutes(request):
    """
    List all routes.
    """
    routes = [
        'GET /api/',
        'GET /api/rooms/',
        'GET /api/rooms/:id/',
        'GET /api/topics/',
        'GET /api/messages/',
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getRoomsOrCreateRoom(request):
    """
    List all rooms, or create a new room.
    """
    if request.method == 'GET':
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(host__username=q) | Q(name__icontains=q) | Q(description__icontains=q))

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def getRoom(request, pk):
        """
        Retrieve, update, or delete a room.
        """
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            data = {"message": "Room does not exist"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = RoomSerializer(room, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = RoomSerializer(room, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response(data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PATCH':
            serializer = RoomSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response(data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            room.delete()
            data = {"message": "Deleted successfully"}
            return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def getTopicsOrCreateTopic(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response(serializer.errors)

@api_view(['GET', 'POST'])
def getMessages(request):
    if request.method == 'GET':
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        try:
            roomID = int(q)
        except:
            roomID = -1

        messages = Message.objects.filter(Q(user__username=q) | Q(room__topic__name__icontains=q) | Q(room__id=roomID))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
