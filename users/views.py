from django.urls import reverse_lazy, reverse
from django.http import request
from allauth.account.signals import user_signed_up
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile, CustomUser
from bucket.settings import AUTH_USER_MODEL
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from .forms import CustomUserCreationForm, UserProForm
from django.contrib import messages







##To send a message to a view ."example is : messages.error(request,'your bla bla bla')"

#Obselete not in use now
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

#Detail Views
# class ProfileDetailView(DetailView):
#     model = UserProfile


class UserProfileUpdateView(UpdateView):

    model = UserProfile
    template_name_suffix = '_update_form'
    form_class = UserProForm
    # fields = ('display_name','description', 'website', 'phone', 'country', 'county', 'image', 'created_date')

    redirect_field_name = '/'

    def get_queryset(self):
        return UserProfile.objects.all()









