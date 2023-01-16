#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
from django import forms
from django.contrib.auth.models import User, permission


class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
user = User.objects.create_superuser(username='neoprospecta', 
                                     email='neoprospecta@example.com',
                                     password='neopct1234')


