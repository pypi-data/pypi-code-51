# Generated by Django 2.1.4 on 2018-12-22 16:56

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion

import django_rebel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(choices=[('accepted', 'accepted'), ('clicked', 'clicked'), ('complained', 'complained'), ('delivered', 'delivered'), ('failed', 'failed'), ('opened', 'opened'), ('rejected', 'rejected'), ('unsubscribed', 'unsubscribed')], max_length=32)),
                ('extra_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email_from', models.CharField(max_length=256)),
                ('email_to', models.CharField(max_length=256)),
                ('message_id', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=32)),
                ('storage_url', models.URLField(blank=True, null=True)),
                ('owner_id', models.PositiveIntegerField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, db_index=True, null=True, size=None)),
            ],
            managers=[
                ('objects', django_rebel.models.MailManager()),
            ],
        ),
        migrations.CreateModel(
            name='MailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=512, null=True)),
                ('body_text', models.TextField(blank=True, null=True)),
                ('body_html', models.TextField(blank=True, null=True)),
                ('body_plain', models.TextField(blank=True, null=True)),
                ('mail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='django_rebel.Mail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MailLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mail',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_rebel.MailLabel'),
        ),
        migrations.AddField(
            model_name='mail',
            name='owner_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='event',
            name='mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='django_rebel.Mail'),
        ),
        migrations.AlterUniqueTogether(
            name='mail',
            unique_together={('email_to', 'message_id')},
        ),
    ]
