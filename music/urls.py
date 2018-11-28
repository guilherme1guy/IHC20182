from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('my_music/', views.MyMusicView.as_view(), name='my_music'),
    path('discover/', views.DiscoverView.as_view(), name='discover'),
    path('detail_music/', views.DetailMusicView.as_view(), name='detail_music'),
    path('detail_album/', views.DetailAlbumView.as_view(), name='detail_album'),
    path('detail_playlist/', views.DetailPlaylistView.as_view(), name='detail_playlist'),
]
