# Generated by Django 2.2 on 2019-06-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basemodels', '0011_auto_20190612_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basemodel',
            options={'ordering': ['-created_at'], 'verbose_name': 'مدل پایه', 'verbose_name_plural': 'مدل های پایه'},
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='review_average',
            field=models.FloatField(default=0.0, verbose_name='میانگین نظرات'),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='مرتب سازی'),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='بروزرسانی شده در'),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='update_needed',
            field=models.BooleanField(default=False, verbose_name='نیاز به بروزرسانی'),
        ),
    ]
