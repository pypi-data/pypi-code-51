# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 13:02


from django.db import migrations, models
import django.db.models.deletion

def load_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "province.json")


def delete(apps, schema_editor):
    # Store = apps.get_model("stores", "Store")
    # Store.objects.all().delete()
    pass

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shahrak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='province.Province')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='province.City')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='province.Province'),
        ),
        migrations.RunPython(
            load_from_fixture,
            delete),
    ]
