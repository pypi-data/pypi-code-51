# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-14 14:38


from django.db import migrations


def username_mention(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    User = apps.get_model('aparnik_users', 'User')
    for user in User.objects.all():
        user.username_mention = user.username
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('aparnik_users', '0013_user_username_mention'),
    ]

    operations = [
        migrations.RunPython(username_mention, reverse_code=migrations.RunPython.noop),
    ]
