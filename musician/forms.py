from django import forms
from django.forms.fields import FileField
from django.forms import ModelForm
from audiofield.widgets import CustomerAudioFileWidget
from audiofield.models import AudioFile

from .models import UploadMusic
from audiofield.widgets import CustomerAudioFileWidget

# class CustomerAudioFileForm(ModelForm):
#     audio_file = forms.FileField(widget=CustomerAudioFileWidget)
#     class Meta:
#         model = AudioFile
#         fields = ['name', 'audio_file']
#         exclude = ('user',)
#
class songupload(ModelForm):
    class Meta:
        model = UploadMusic
        fields = ['composer','title', 'audio_file']
        exclude = ('user',)

