# Generated by Django 2.2 on 2019-12-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaging',
            name='uri',
            field=models.CharField(max_length=255, null=True, verbose_name='URI'),
        ),
    ]
