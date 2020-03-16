# Generated by Django 2.1.7 on 2019-05-27 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModelScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='djangoarticle')),
                ('title', models.CharField(max_length=95)),
                ('slug', models.CharField(max_length=95, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('shortlines', models.TextField()),
                ('content', models.TextField()),
                ('verification', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('withdrow', 'Withdorw')], default='draft', max_length=20)),
                ('is_promote', models.BooleanField(default=False)),
                ('is_trend', models.BooleanField(default=False)),
                ('total_views', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Djangoarticle article',
                'verbose_name_plural': 'Djangoarticle articles',
                'ordering': ['serial', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='CategoryModelScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=35, unique=True)),
                ('slug', models.SlugField(max_length=35, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('withdrow', 'Withdorw')], default='draft', max_length=20)),
                ('verification', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Djangoarticle category',
                'verbose_name_plural': 'Djangoarticle categories',
                'ordering': ['serial', 'pk'],
            },
        ),
        migrations.AddField(
            model_name='articlemodelscheme',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoarticle.CategoryModelScheme'),
        ),
    ]
