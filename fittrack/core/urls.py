# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),                 # public landing
    path('register/', views.register, name='register'),      # register page
    path('login/', views.login_view, name='login'),          # login page
    path('logout/', views.logout_view, name='logout'),       # clear session
    path('home/', views.home, name='home'),                  # user home (requires login)
    path('trainings/', views.trainings, name='trainings'),   # trainings page
]
