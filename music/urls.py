from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('my_music/', views.MyMusicView.as_view(), name='my_music'),
    path('discover/', views.DiscoverView.as_view(), name='discover'),
]
