# Generated by Django 4.1.7 on 2023-08-05 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayerRm', '0002_remove_prayerrm_admin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prayerrm',
            name='admin',
            field=models.ManyToManyField(related_name='group_admins', to=settings.AUTH_USER_MODEL),
        ),
    ]
