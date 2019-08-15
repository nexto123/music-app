from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.utils import timezone, datetime_safe
from django.db import models
from bucket.settings import AUTH_USER_MODEL
from django_countries.fields import CountryField
from django.forms import ModelForm, Textarea, CharField



class CustomUser(AbstractUser):
    pass


#Will be added later
COUNTY_MULTIPLE_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class UserProfile(models.Model):

    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200, default='')
    description = models.TextField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='https//:')
    country = CountryField(blank_label='(select country)', default='Country')
    county = models.CharField(max_length=150, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    created_date = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse("profile_edit", kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username




#This class must go into shop models
class Offer(models.Model):
    pass


@receiver(user_signed_up)
def CreateProfile(sender, **kwargs):
    if user_signed_up:
        user_profile = UserProfile.objects.create(user=kwargs['user'])

post_save.connect(CreateProfile, sender = User)


