

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile-edit/', views.profile_edit, name='profile_edit'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('companies/', views.companies, name='companies'),
    path('company/<slug>/', views.company, name='company'),
    path('text-ads/', views.text_ads, name='text_ads'),
    path('text-ad/<slug>/', views.text_ad, name='text_ad'),
    path('video-ads/', views.video_ads, name='video_ads'),
    path('video-ad/<slug>/', views.video_ad, name='video_ad'),




]
