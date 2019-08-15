import re
import time
from datetime import datetime, timedelta
from django.conf import settings
from django import forms
from django.forms import ValidationError
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.password_validation import validate_password
from allauth.account.adapter import app_settings
from allauth.account.signals import user_signed_up, user_logged_in
from django.shortcuts import resolve_url
from django.shortcuts import redirect, reverse



class MyAccountAdapter(DefaultAccountAdapter):

    def clean_password(self, password, user=None):
        min_length = app_settings.PASSWORD_MIN_LENGTH

        if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$', password):
            return password
        else:
            raise forms.ValidationError(("Password must be a minimum of 6 "
                                          "characters. & must start with a Capital letter..").format(min_length))

### PROBLEM NOT RESOLVED YET. LOGIC IMCOMPLETE

    def get_login_redirect_url(self, request):
        threshold = 90  # seconds
        path = ""

        if user_signed_up and (request.user.last_login - request.user.date_joined).seconds < threshold:
            path="/users/profile/{user_id}/edit"
            print('checking')
        else:
            print('you are login')
            return reverse('home')

        return path.format(user_id = request.user.userprofile.pk)