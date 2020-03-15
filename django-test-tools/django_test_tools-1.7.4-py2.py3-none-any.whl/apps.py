# -*- coding: utf-8
from django.apps import AppConfig




class DjangoTestToolsConfig(AppConfig):
    name = 'django_test_tools'

    def ready(self):
        from django_test_tools.checks import example_check

