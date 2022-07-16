from django.urls import path
from trackApp import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('aboutapp',views.aboutapp,name='aboutapp'),
    path('quickguide',views.quickguide,name='quickguide'),
    path('logout',views.logout_view,name="logout_view"),
]
