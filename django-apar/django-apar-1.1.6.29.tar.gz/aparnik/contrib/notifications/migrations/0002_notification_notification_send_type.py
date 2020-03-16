# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-17 16:50


import aparnik.contrib.notifications.models
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_send_type',
            field=django_enumfield.db.fields.EnumField(blank=True, default=0, enum=aparnik.contrib.notifications.models.NotificationType, null=True, verbose_name='Notification send type'),
        ),
    ]
