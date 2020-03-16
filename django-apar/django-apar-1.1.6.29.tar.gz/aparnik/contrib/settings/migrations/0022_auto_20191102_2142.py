# Generated by Django 2.2 on 2019-11-02 21:42

from django.db import migrations

def add_keys(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Setting = apps.get_model('settings', 'Setting')
    key = ''
    try:
        key = 'BANK_MELLI_MERCHENT_CODE'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='مرچنت کد بانک ملی',
            key=key,
            value='',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'BANK_MELLI_TERMINAL_CODE'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='ترمینال کد بانک ملی',
            key=key,
            value='',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'BANK_MELLI_SECRET_KEY'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title=' کلید خصوصی بانک ملی',
            key=key,
            value='',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )



def remove_keys(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Setting = apps.get_model('settings', 'Setting')
    try:
        key = 'BANK_MELLI_SECRET_KEY'
        Setting.objects.get(key=key).delete()
    except Exception:
        pass

    try:
        key = 'BANK_MELLI_TERMINAL_CODE'
        Setting.objects.get(key=key).delete()
    except Exception:
        pass

    try:
        key = 'BANK_MELLI_MERCHENT_CODE'
        Setting.objects.get(key=key).delete()
    except Exception:
        pass



class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0021_auto_20190717_1017'),
    ]

    operations = [
        migrations.RunPython(add_keys, reverse_code=remove_keys),
    ]
