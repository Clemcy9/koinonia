# Generated by Django 4.1.7 on 2023-08-05 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prayerRm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayerrm',
            name='admin',
        ),
    ]