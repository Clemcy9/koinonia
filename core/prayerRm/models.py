from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()
class PrayerRm(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(user)
    admin = models.ForeignKey(user,related_name='admin_group', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Chats(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING, null=True, blank=True)
    message = models.TextField()
    group = models.ForeignKey(PrayerRm, on_delete=models.DO_NOTHING,null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user + self.time_stamp