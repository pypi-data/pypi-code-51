# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-10 15:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category', verbose_name='\\u062f\\u0633\\u062a\\u0647 \\u0628\\u0646\\u062f\\u06cc \\u0647\\u0627'),
        ),
    ]
