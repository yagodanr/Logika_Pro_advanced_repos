#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm_blog.settings")
django.setup()