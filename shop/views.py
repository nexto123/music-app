from django.views.generic import TemplateView, ListView
from users.models import UserProfile
from musician.models import UploadMusic
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = 'home.html'


class profile_list(ListView):
    model = UserProfile
    template_name = 'userprofile_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(created_date__lte=timezone.now())