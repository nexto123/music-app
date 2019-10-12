from django.contrib import admin
from musician.models import UploadMusic
from audiofield.admin import AudioFileAdmin
from .models import UploadMusic

import os

admin.site.register(UploadMusic)
