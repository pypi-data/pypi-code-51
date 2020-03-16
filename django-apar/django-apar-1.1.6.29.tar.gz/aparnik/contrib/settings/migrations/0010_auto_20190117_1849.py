# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-17 18:49


from django.db import migrations


def add_keys(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Setting = apps.get_model('settings', 'Setting')

    key = ''
    try:
        key = 'DOLLAR_TO_IRR'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='معادل دلار به ریال',
            key=key,
            value='130000',
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_auto_20190115_2118'),
    ]

    operations = [
        migrations.RunPython(add_keys, reverse_code=migrations.RunPython.noop),
    ]
