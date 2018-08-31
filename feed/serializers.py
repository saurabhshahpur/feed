from rest_framework import serializers

from feed.models import UserDetail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail