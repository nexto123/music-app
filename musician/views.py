from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView,FormView)

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .forms import songupload
from .models import UploadMusic
from django.utils import timezone
# from users.models import UserProfile, CustomUser
# from users.views import UserProfileUpdateView
# from django.shortcuts import get_object_or_404
# from django.conf import settings
# from audiofield.fields import AudioField
# from audiofield.models import AudioFile
# from django.urls import reverse
# from bucket.settings import AUTH_USER_MODEL
# from django.contrib.auth.models import User

# import os.path
# from audiofield.widgets import CustomerAudioFileWidget
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import get_user_model
# from django.http import HttpResponseRedirect

#Will be added soon.
from django.contrib.auth.mixins import LoginRequiredMixin

### Restructure the models and use less user connection.
#Create form view
# @login_required
# def song_form(request):
#     template = 'musician/uploadsong_update_form.html'
#     form = songupload
#
#     # Add audio
#     if request.method == 'POST':
#         form = songupload(request.POST, request.FILES)
#         if form.is_valid():
#
#             obj = form.save(commit=False)
#             user = get_user_model()
#             obj.user = get_user_model().objects.get(username=request.user)
#
#             return HttpResponseRedirect('/')
#
#         # To retain frontend widget, if form.is_valid() == False
#         form.fields['audio_file'].widget = CustomerAudioFileWidget()
#
#     data = {
#        'form': form,
#     }
#
#     return render(request,template, data)
#
#

# class SongForm(CreateView):
#     models = UploadMusic
#     fields = ['title','description','album_cover','audio_file']
#     template_name = 'musician/uploadsong_update_form.html'
#     # success_url = 'users:profile_edit'
#
#     def get_queryset(self):
#         return UploadMusic.objects.all()
#
#     def form_valid(self, form):
#         song = get_object_or_404(UploadMusic, pk=self.kwargs['pk'])
#         form.instance.song = song
#         return super(SongForm, self).form_valid(form)





class playnow(TemplateView):
    template_name = 'musician/music_player.html'


#list view of song ALbum

class song_list(ListView):
    models = UploadMusic

    def get_queryset(self):
        return UploadMusic.objects.filter(created_date__lte=timezone.now())


#Update view and form view
class UploadSong(UpdateView):

    model = UploadMusic
    template_name = 'musician/uploadsong_update_form.html'
    # template_name_suffix = '_update_form'
    form_class = songupload

    redirect_field_name = '/'

    def get_queryset(self):
        return UploadMusic.objects.all()




def case(request):
    man = UploadMusic.objects.get()
    print(man.title)

