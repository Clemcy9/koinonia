from django.db import models

# Create your models here.

class PrayerRm(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(, null=True, blank=True)
    admin = models.ForeignKey()

    def __str__(self) -> str:
        return self.name
    
class Chats(models.Model):
    user = models.OneToOneField()
    message = models.TextField()
    group = models.ForeignKey(PrayerRm, on_delete=models.DO_NOTHING,null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user + self.time_stamp