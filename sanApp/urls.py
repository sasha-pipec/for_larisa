from django.contrib import admin
from django.urls import path
from sanApp.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail'),

    path('review/', ReviewCreateView.as_view(), name='create_comment'),

    path('login/', UserLoginRender.as_view(), name='login'),
    path('user/login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegisterRender.as_view(), name='register'),
    path('user/register/', UserRegisterView.as_view(), name='user_register'),
]
