from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('group/', views.GroupView.as_view(), name='group'),
]
