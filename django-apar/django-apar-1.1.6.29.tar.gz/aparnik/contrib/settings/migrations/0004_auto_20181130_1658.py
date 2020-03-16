# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 16:58


from django.db import migrations


def add_keys(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Setting = apps.get_model('settings', 'Setting')

    key = ''
    try:
        key = 'LOGO_PROJECT_ICON'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='لوگو',
            key=key,
            value='https://cdn.aparnik.com/static/website/img/logo-persian.png',
            value_type='s',
            is_show=True,
            is_variable_in_home=True,
        )

    try:
        key = 'SERVER_NAME'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='آدرس سایت',
            key=key,
            value='api.aparnik.com',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'SERVER_PORT'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='پورت سایت',
            key=key,
            value='80',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'PRODUCT_WALLET_ID'
        Setting.objects.get(key=key)
    except Exception:
        Product = apps.get_model('products', 'Product')
        ContentType = apps.get_model('contenttypes', 'ContentType')

        product = Product.objects.create(price_fabric=1, title='شارژ کیف پول')

        new_ct = ContentType.objects.get_for_model(Product)
        Product.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)

        Setting.objects.create(
            title='شارژ کیف پول',
            key=key,
            value=str(product.id),
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'COURSE_LEVEL'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='سطح دوره',
            key=key,
            value='2',
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'INVITER_GIFT_CREDITS_PER_PURCHASE'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='درصد اعتبار هدیه برای دعوت کننده به ازای هر خرید',
            key=key,
            value='0',
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'INVITER_GIFT_CREDITS'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='اعتبار هدیه برای دعوت کننده در بدو قبول دعوت تومان',
            key=key,
            value='0',
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'INVITED_GIFT_CREDITS'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='اعتبار هدیه برای دعوت شونده در بدو قبول دعوت تومان',
            key=key,
            value='0',
            value_type='i',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'PRICE_FORMAT'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='اعتبار هدیه برای دعوت کننده در بدو قبول دعوت تومان',
            key=key,
            value='%ic=t:%se=,:%cu=t:%gr=3:%tr=True:%abbr=True',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'PRICE_PRODUCT_FREE_DESCRIPTION'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='عنوان کالاهای رایگان',
            key=key,
            value='رایگان',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'PRICE_PRODUCT_SHARING_DESCRIPTION'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='عنوان کالاهایی که دعوت شده اند',
            key=key,
            value='دعوت شده',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'PRICE_PRODUCT_BUY_DESCRIPTION'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='عنوان کالاهای خریداری شده',
            key=key,
            value='خریداری شده',
            value_type='s',
            is_show=False,
            is_variable_in_home=False,
        )

    try:
        key = 'AWS_ACTIVE'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='آمازون',
            key=key,
            value='AWS_ACTIVE',
            value_type='fr',
            is_show=False,
            is_variable_in_home=True,
        )

    try:
        key = 'USER_LOGIN_WITH_PASSWORD'
        Setting.objects.get(key=key)
    except Exception:
        Setting.objects.create(
            title='ورود با رمز عبور',
            key=key,
            value='USER_LOGIN_WITH_PASSWORD',
            value_type='fr',
            is_show=False,
            is_variable_in_home=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20181125_1109'),
    ]

    operations = [
        migrations.RunPython(add_keys, reverse_code=migrations.RunPython.noop),
    ]
