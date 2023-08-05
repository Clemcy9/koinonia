from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommunitySerializer
from .models import Community

# Create your views here.

# api starts

class CommunityView(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# api ends
