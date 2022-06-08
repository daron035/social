from django.shortcuts import render, redirect

from .models import *
from .forms import *


def dashboard(request):
    # a = request.user 
    # print(a)
    # print(a.id)
    # # print(a.tweets.all().values('body'))
    # print(a.tweets.get(id=5).body)
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

    return render(request, 'chitter/dashboard.html', {'form': form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    # profiles = Profile.objects.all()
    form = TweetsForm
    dashboard(request)
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
        current_user.save()
    form = TweetsForm
    return render(request, 'chitter/profile.html', {'profile': profile, 'form': form})

# def profile_tweet_redirect(request):
