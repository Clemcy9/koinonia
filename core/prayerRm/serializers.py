from rest_framework import serializers
from .models import PrayerRm

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRm
        fields = ['id','name', 'participants','admin','chats_set']

        depth = 1