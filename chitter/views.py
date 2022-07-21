from django.http import HttpResponseRedirect  # REDIRECT TO SAME PAGE
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views.generic import ListView
import logging

from .models import *
from user.models import User
from .forms import *


logger = logging.getLogger('main')

def home(request):
    
    a = request.META.get('REMOTE_ADDR')
    # logger.info(f"home {a}")
    # logger.info("hello")
    logger.info(f"home", extra={"ip": a})

    if not request.user.is_authenticated:
        return redirect('public_profile_list')

    form = TweetsForm
    if request.method == 'POST':
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')

    q = Profile.objects.get(user=request.user)
    profiles = (q.friends.all()).union(q.follows.all())

    return render(request, 'chitter/home.html', {'form': form, 'profiles': profiles})


def public_profile_list(request):
    a = request.META.get('REMOTE_ADDR')

    if request.user.is_authenticated:
        logger.info(f"public_authenticated", extra={"ip": a})
    elif not request.user.is_authenticated:
        logger.info(f"not_authenticated", extra={"ip": a})
    else:
        logger.info(f"EXCEPTION", extra={"ip": a})
    profiles = Profile.objects.all()

    return render(request, 'chitter/public_profile_list.html', {'profiles': profiles})


# REDIRECT TO the SAME PAGE
@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    form = TweetsForm

    if request.method == 'POST':  # form tweet
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            # REDIRECT TO the SAME PAGE
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'chitter/profile_list.html', {'profiles': profiles, 'form': form})


@login_required
def user_follows_list(request):
    profiles = Profile.objects.get(user=request.user)
    return render(request, 'chitter/user_follows_list.html', {'profiles': profiles})


@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':  # form tweet
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(profile.get_absolute_url())
        current_user = request.user.profile  # form follow to user
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user.follows.add(profile)
        elif action == 'unfollow':
            current_user.follows.remove(profile)
        elif action == 'delete':
            current_user.friends.remove(profile)
            profile.friends.remove(current_user)
        current_user.save()
        # REDIRECT TO the SAME PAGE
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = TweetsForm
    return render(request, 'chitter/profile.html', {'profile': profile, 'form': form})


class UserList(ListView):
    model = Profile
    template_name = 'chitter/all_users_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().order_by('user__username')

def user_friends_list(request):
    profiles = Profile.objects.get(user=request.user)
    requests = FriendRequest.objects.filter(receiver=request.user)
    return render(request, 'chitter/user_friends_list.html', {'profiles': profiles, 'requests': requests})


@login_required
def send_friend_request(request, pk):
    sender = request.user
    receiver = Profile.objects.get(pk=pk)
    obj, created = FriendRequest.objects.get_or_create(
        sender=sender, receiver=receiver.user)

    if created:
        return HttpResponse('friend request send')
    else:
        return HttpResponse('friend request already send')


@login_required
def accept_friend_request(request, pk):
    # добавляем первому юзеру в профиль друга(профиль)
    user = request.user.profile
    new_user = User.objects.get(pk=pk)
    user.friends.add(new_user.profile)
    # добавляем добавленному другу в его профиль первого юзера профиль 
    # id1 2:1
    # id2 1:2
    new_user_profile = Profile.objects.get(user=new_user)
    new_user_profile.friends.add(user)
    FriendRequest.objects.get(sender=new_user).delete()
    return redirect('user_friends_list')


@login_required
def decline_friend_request(request, pk):
    new_user = User.objects.get(pk=pk)
    FriendRequest.objects.get(sender=new_user).delete()
    return redirect('user_friends_list')


def resume(request):
    return render(request, 'resume')