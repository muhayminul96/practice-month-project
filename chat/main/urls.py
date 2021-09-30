
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('room/<str:room>', views.chat, name='room'),
    path('register', views.register, name='register'),
    path('login', views.signin, name='login'),
    path('logout', views.log_out, name='logout'),
    path('accounts/login/', views.register, name='register'),
]