# Generated by Django 5.0.2 on 2024-02-09 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='profileId',
        ),
    ]
