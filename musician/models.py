from django.db import models
from users.models import UserProfile, CustomUser
from bucket.settings import AUTH_USER_MODEL
from datetime import datetime
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from audiofield.fields import AudioField
from django.conf import settings
import os.path

### Must use django signals to create these models when user is created

class UploadMusic(models.Model):
  userprofile = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  album_cover = models.ImageField(upload_to='album_cover/%Y/%m/%d/')
  audio_file = AudioField(upload_to='media/songs/', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

  created_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title

  def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
      file_url = settings.MEDIA_URL + str(self.audio_file)
      player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
      return player_string


  audio_file_player.allow_tags = True
  audio_file_player.short_description = ('Audio file player')

#
# class PhotoBucket(models.Model):
#
#   photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
#   photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#   description = models.TextField(blank=True)
#   def __str__(self):
#     return self.name




@receiver(user_signed_up)
def CreateProfile(sender, **kwargs):
    if user_signed_up:
        user_profile = UserProfile.objects.create(user=kwargs['user'])

post_save.connect(CreateProfile, sender = User)



##Must complete and migrate to database