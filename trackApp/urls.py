from django.urls import path
from trackApp import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
]
