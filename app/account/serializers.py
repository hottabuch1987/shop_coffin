from rest_framework import serializers
from .models import User, UserDead


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserDeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDead
        fields = ('__all__')