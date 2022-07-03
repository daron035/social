from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls.base import reverse_lazy
import json

from chitter.models import Profile
from .models import Message, PrivateChatRoom
from .utils import *

from user.models import User


def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'chat/index.html', {'profile': profile})


def room(request, room_id):
    username = request.user.username
    messages = Message.objects.filter(room=room_id)[0:25]
    room_id = PrivateChatRoom.objects.get(id=room_id)

    return render(request, 'chat/room.html', {'room_id': room_id, 'username': username, 'messages': messages})


def create_or_return_private_chat(request, pk):
    user1 = request.user
    payload = {}
    if user1.is_authenticated:
        if request.method == "GET":
            user2_id = request.GET.get(pk)
            print(user2_id)
            try:
                user2 = User.objects.get(pk=pk)
                chat = find_or_create_private_chat(user1, user2)
                print("Successfully got the chat.")
                payload['response'] = "Successfully got the chat."
                payload['chatroom_id'] = chat.pk
                return redirect('room', chat.pk)
            except Exception as e:
                payload['response'] = "Unable to start a chat with that user."
                print(e)
    else:
        payload['response'] = "You can't start a chat if you are not authenticated."

    return HttpResponse(json.dumps(payload), content_type="application/json")
