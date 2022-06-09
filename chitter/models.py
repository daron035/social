from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from user.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True)
    friends = models.ManyToManyField(
        'self', related_name='friends_by', symmetrical=False, blank=True)
    

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: # provides post_save
        user_profile = Profile(user=instance)
        user_profile.save()

        # user_profile = Profile(user=instance)
        # user_profile.save()
        # user_profile.follows.add(instance.profile) or .set([instance.profile.id])
        # user_profile.save()

# Create a Profile for each new user.
# post_save.connect(create_profile, sender=User)


class Tweets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    body = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tweets'

    def time_admin(self):
        return f"{self.created_at:%d-%m-%Y %H:%M}"


class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")