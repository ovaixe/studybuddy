from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from base.models import Room, Topic, Message
from .serializers import RoomSerializer, TopicSerializer, MessageSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms/',
        'GET /api/rooms/:id/',
        'GET /api/topics/',
        'GET /api/messages/',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(host__username=q) | Q(name__icontains=q) | Q(description__icontains=q))

    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    try:
        roomID = int(q)
    except:
        roomID = -1

    messages = Message.objects.filter(Q(user__username=q) | Q(room__topic__name__icontains=q) | Q(room__id=roomID))

    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTopic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data)
    return Response(serializer.errors)

@api_view(['POST'])
def createRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data)
    else:
        print(serializer.data)
        return Response(serializer.errors)