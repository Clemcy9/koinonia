from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    pass

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User,default=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length=16)
    profile_pics = models.ImageField('Profile Picture',upload_to='./static/profile', null=True)

    def __str__(self):
        return str(self.user)
    

def create_profile(user):
    pass

def get_profile(user):
    pass

def delete_profile(user):
    pass