from rest_framework import serializers

from user.models import User
from chitter.models import Tweets


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'first_name', 'last_name')

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'