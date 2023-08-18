from django.shortcuts import render
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate

from rest_framework import viewsets, generics,views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from allauth.account import views as allauth_view

# for dj_rest_auth with google
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here. 

# # api start

@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
   
# login view
class LoginView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response('login route')
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f'email={email}, password ={password}')
        user = authenticate(email=email, password=password)
        # user = User.objects.get(email=email)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'detail': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED )

# loginview allauth library


@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    user = request.user
    token = Token.objects.get(user=user)
    token.delete()
    return Response({'detail':'logout successfully'}, status= status.HTTP_200_OK)


# using allauth
# class LoginV

class LogoutView(views.APIView,allauth_view.LogoutView):
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
    
# dj_rest_auth apis
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = '/home'
    client_class = OAuth2Client



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
