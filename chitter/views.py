from django.shortcuts import render

from .models import Profile


def dashboard(request):
    return render(request, 'chitter/dashboard.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    # profiles = Profile.objects.all()
    return render(request, 'chitter/profile_list.html', {'profiles': profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user.follows.add(profile)
        elif action == 'unfollow':
            current_user.follows.remove(profile)
        current_user.save()
    return render(request, 'chitter/profile.html', {'profile': profile})