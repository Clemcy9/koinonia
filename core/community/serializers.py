from rest_framework import serializers
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField()
    admins = serializers.StringRelatedField()
    class Meta:
        model = Community
        fields = '__all__'

        # depth = 1