from .models import User, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= User,)
def create_user_profile(sender, instance, created, **kwargs):
    print(f'from signals, sender={sender}\ninstance={instance}\ncreated={created}\nkwargs={kwargs}')
    if created:
        Profile.objects.create(user=instance)

