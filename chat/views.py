from django.shortcuts import render

from chitter.models import Profile
from .models import Message

from user. models import User


def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'chat/index.html', {'profile': profile})


def room(request, room_name):
    username = request.user.username
    messages = Message.objects.filter(room=room_name)[0:25]

    a = room_name
    messages2 = User.objects.get(username=a)
    messages2 = Message.objects.filter(room=messages2)[0:25]

    # username = request.user.username
    # a = room_name
    # messages2 = User.objects.get(username=a)

    # messages = Message.objects.filter(room=room_name)[0:25] | Message.objects.filter(room=messages2)[0:25]
    # # messages2 = Message.objects.filter(room=messages2)[0:25]

    # print('AAAAAAAAAAAA', messages2)
    # print(type(messages2))
    
    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})