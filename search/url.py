from django.urls import path, include
from . import views

app_name='search'
urlpatterns = [
    path('', views.FirstPageSearchView.as_view(), name='first_page_search'),
    path('result/',views.SearchView.as_view(), name='result'),
]
