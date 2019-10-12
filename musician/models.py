from django.db import models
from users.models import UserProfile, CustomUser
from bucket.settings import AUTH_USER_MODEL
from datetime import datetime
from django.contrib.auth.models import User
from users.models import UserProfile
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from audiofield.fields import AudioField
from django.conf import settings
from django.urls import reverse
from multiselectfield import MultiSelectField
import os.path

### Must use django signals to create these models when user is created

GENRE_CHOICES = [
    ('Blues','Blues'),
    ('Raggae','Raggae'),
    ('Rock lover','Rock lover'),
    ('Rock Jazz','Rock Jazz'),
    ('Slow Jam','Slow Jam'),
    ('Jazz','Jazz'),
    ('Samba','Samba'),
    ('Afro Jazz','Afro Jazz'),
]


class UploadMusic(models.Model):
  user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  composer = models.CharField(max_length=200, default='')
  description = models.TextField(blank=True)
  album_cover = models.ImageField(upload_to='album_cover/%Y/%m/%d/')
  genre = models.CharField(max_length=30, default='select a genre',choices=GENRE_CHOICES)
  audio_file = AudioField(upload_to='media/songs/',blank=False,null=False,default='',
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

  created_date = models.DateTimeField(default=datetime.now, blank=True)
  allow_listening = models.BooleanField(default=True)
  def get_absolute_url(self):
      return reverse("song_update", kwargs={'pk': self.pk})

  def __str__(self):
    return self.user.username


  def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
      file_url = settings.MEDIA_URL + str(self.audio_file)
      player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
      return player_string


  audio_file_player.allow_tags = True
  audio_file_player.short_description = ('Audio file player')




# # We are using signals to create the form for this models just so we can avoid the need to use a CreateView template, which will be different
@receiver(user_signed_up)
def CreateUploadSong(sender, **kwargs):
    if user_signed_up:
        upload_music = UploadMusic.objects.create(user=kwargs['user'])

post_save.connect(CreateUploadSong, sender = User)
