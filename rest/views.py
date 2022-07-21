from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from chitter.models import User
from .serializers import *


class ProfileViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.all()

class TweetsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer

    def get_queryset(self):
        return Tweets.objects.all()