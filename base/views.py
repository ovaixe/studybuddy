from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Room, Topic, Message
from .forms import RoomForm, CustomUserCreationForm, UserForm, UserProfileForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
        except Exception as e:
            print("[Exception raised]: ", e)
            messages.error(request, "User does not exist")

    context = {'page': page}
    return render(request, 'base/pages/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'base/pages/login_register.html', context)


def home(request):
    q = request.GET.get('q')
    if not q:
        q = ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(
        name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q)
    )

    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count,
               'room_messages': room_messages, 'q': q}
    return render(request, 'base/pages/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'base/pages/room.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}

    return render(request, 'base/pages/profile.html', context)


@login_required(login_url='user-login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/pages/room_form.html', context)


@login_required(login_url='user-login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        messages.error(request, "You are not allowed here!!!")
        return redirect('home')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/pages/room_form.html', context)


@login_required(login_url='user-login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        messages.error(request, "You are not allowed here!!!")
        return redirect('home')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/pages/delete.html', {'obj': room})


@login_required(login_url='user-login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        messages.error(request, "You are not allowed here!!!")
        return redirect('home')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    context = {'obj': message}
    return render(request, 'base/pages/delete.html', context)


@login_required(login_url='user-login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    profileForm = UserProfileForm(instance=user.userprofile)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        profileForm = UserProfileForm(
            request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid() and profileForm.is_valid():
            form.save()
            profileForm.save()
            return redirect('user-profile', pk=user.id)
        else:
            messages.error(request, 'An error occured during profile update')

    context = {'form': form, 'profile_form': profileForm}
    return render(request, 'base/pages/update-user.html', context)
