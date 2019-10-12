from django.urls import path
from musician import views
# from musician.views import song_form

urlpatterns = [
    path('case/', views.case),
    path('songlist/', views.song_list.as_view(), name='song_list'),
    path('update-song/<int:pk>/', views.UploadSong.as_view(), name='song_update'),
    # path('uploadform/', views.song_form, name="upload_music")
    # path('test-player/', views.player.as_view()),
]

