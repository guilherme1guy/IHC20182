from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyMusicView.as_view(), name='my_music'),
]
