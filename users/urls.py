from django.urls import path, reverse
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/edit', views.UserProfileUpdateView.as_view(), name='profile_edit'),
]