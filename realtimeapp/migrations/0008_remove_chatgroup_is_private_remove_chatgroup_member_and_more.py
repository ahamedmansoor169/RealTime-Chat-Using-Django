# Generated by Django 5.0.6 on 2024-06-26 10:38

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtimeapp', '0007_chatgroup_is_private_chatgroup_member_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='member',
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=500, unique=True),
        ),
    ]
