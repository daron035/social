from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from user.models import User
from .forms import *


def dashboard(request):
    # a = request.user 
    # print(a)
    # print(a.id)
    # # print(a.tweets.all().values('body'))
    # print(a.tweets.get(id=5).body)
    if not request.user.is_authenticated:
        return redirect('public_profile_list')

    if request.method == 'POST':
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('dashboard')
    form = TweetsForm

    # req_user_id = request.user
    
    # SELECT 
    # tweet = User.objects.
    q = Profile.objects.get(user=request.user)
    qs2 = q.friends.all()
    print('\n',qs2, '\n')

    print(q.friends.all())
    return render(request, 'chitter/dashboard.html', {'form': form, 'qs2': qs2})

def public_profile_list(request):
    profiles = Profile.objects.all()
    # form = TweetsForm

    return render(request, 'chitter/public_profile_list.html', {'profiles': profiles})

# REDIRECT TO SAME PAGE
from django.http import HttpResponseRedirect # REDIRECT TO SAME PAGE
# REDIRECT TO SAME PAGE

def profile_list(request):

    # if not request.user.is_authenticated:
    #     return redirect('public_profile_list')
        
    profiles = Profile.objects.all()
    # profiles = Profile.objects.exclude(user=request.user)
    form = TweetsForm

    if request.method == 'POST': # форма твита
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'chitter/profile_list.html', {'profiles': profiles, 'form': form})

def user_follows_list(request):
    profiles = Profile.objects.get(user=request.user)
    # profiles = Profile.objects.all()
    return render(request, 'chitter/user_follows_list.html', {'profiles': profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST': # форма твита
        form = TweetsForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(profile.get_absolute_url())
        current_user = request.user.profile # форма подписки на пользователя
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user.follows.add(profile)
        elif action == 'unfollow':
            current_user.follows.remove(profile)
        elif action == 'delete':
            current_user.friends.remove(profile)
        current_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # REDIRECT TO SAME PAGE
    form = TweetsForm
    return render(request, 'chitter/profile.html', {'profile': profile, 'form': form})


def user_friends_list(request):
    profiles = Profile.objects.get(user=request.user)
    requests = FriendRequest.objects.filter(receiver=request.user)
    return render(request, 'chitter/user_friends_list.html', {'profiles': profiles, 'requests': requests})


@login_required
def send_friend_request(request, pk):
    sender = request.user
    receiver = User.objects.get(id=pk)
    obj, created = FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)

    if created:
        return HttpResponse('friend request send')
    else:
        return HttpResponse('friend request already send')

@login_required
def accept_friend_request(request, pk):
    user = request.user.profile
    new_user = User.objects.get(pk=pk)
    user.friends.add(new_user.profile)
    FriendRequest.objects.get(sender=new_user).delete()
    return redirect('user_friends_list')

@login_required
def decline_friend_request(request, pk):
    new_user = User.objects.get(pk=pk)
    FriendRequest.objects.get(sender=new_user).delete()
    return redirect('user_friends_list')