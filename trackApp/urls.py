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
<<<<<<< HEAD
    path('logout',views.logout_view,name="logout_view"),
    path('createproject',views.createproject,name="createproject"),
    path('joinproject',views.joinproject,name="joinproject"),
    path('currentprojects',views.currentprojects,name="currentprojects"),
=======
    path('logout',views.logout_view,name='logout_view'),
    path('createProject',views.createProject,name='createProject'),
    path('joinProject',views.joinProject,name='joinProject'),
    path('myProjects',views.myProjects,name='myProjects'),
>>>>>>> 1e1f36778459fd90ff9cf122691b8aa021c2e867
]
