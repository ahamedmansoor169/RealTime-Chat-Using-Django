# Generated by Django 5.0.6 on 2024-06-26 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtimeapp', '0004_chatgroup_users_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='users_online',
        ),
    ]
