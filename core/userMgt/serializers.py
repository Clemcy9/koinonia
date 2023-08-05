from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'

        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1