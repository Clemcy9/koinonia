from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
# Create your views here.

# api start
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
   


#api end


def create_user(request):
    pass

def get_user(request):
    pass

def update_user(request):
    pass

def delete_user(request):
    # set active to false, dont delete user
    pass
