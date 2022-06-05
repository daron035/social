from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

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