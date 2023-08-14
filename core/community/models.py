from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    admins =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='admin',on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


# churh
# name
# logo
# email


# team