

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login_page, name='login'),
    path('profile', views.profile, name='profile'),
    path('profile-edit', views.profile_edit, name='profile_edit'),




]
