from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SignInView.as_view(), name='sign_in'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('help_page/', views.HelpPage.as_view(), name='help_page'),
    path('instruction/', views.InstructionPage.as_view(), name='instruction_page'),
]
