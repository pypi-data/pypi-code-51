# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-24 11:00
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models

import model_utils.fields

NEW_SOURCE_NAME = 'Enterprise management command enrollment'
NEW_SOURCE_SLUG = 'management_command'


def update_source(apps, schema_editor):
    """
    The name of this Source is being updated to better reflect it usage.
    """
    enrollment_sources = apps.get_model('enterprise', 'EnterpriseEnrollmentSource')
    enrollment_sources.objects.create(name=NEW_SOURCE_NAME, slug=NEW_SOURCE_SLUG)


def revert_source(apps, schema_editor):
    """
    The name of this Source is being updated to better reflect it usage.
    """
    enrollment_sources = apps.get_model('enterprise', 'EnterpriseEnrollmentSource')
    enrollment_sources.objects.get(name=NEW_SOURCE_NAME, slug=NEW_SOURCE_SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0079_AddEnterpriseEnrollmentSource'),
        ('enterprise', '0081_UpdateEnterpriseEnrollmentSource'),
    ]

    operations = [
        migrations.RunPython(update_source, revert_source)
    ]
