# Generated by Django 2.1.10 on 2019-10-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0183_auto_20191020_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='expertus_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Identyfikator w bazie Expertus'),
        ),
    ]
