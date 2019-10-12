from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('profilelist/', views.profile_list.as_view(), name='profile_list'),
]