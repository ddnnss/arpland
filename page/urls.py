

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile-edit/', views.profile_edit, name='profile_edit'),
    path('profile-add-text/<id>', views.profile_add_text, name='profile_add_text'),
    path('profile-add-video/<id>', views.profile_add_video, name='profile_add_video'),
    path('profile-add-bl/', views.profile_add_bl, name='profile_add_bl'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('companies/', views.companies, name='companies'),
    path('company-info/<slug>/', views.company_info, name='company_info'),
    path('text-ads/', views.text_ads, name='text_ads'),
    path('text-ad/<slug>/', views.text_ad, name='text_ad'),
    path('video-ads/', views.video_ads, name='video_ads'),
    path('video-ad/<slug>/', views.video_ad, name='video_ad'),
    path('blacklist/', views.blacklist_all, name='blacklist_all'),
    path('blacklist/<slug>/', views.blacklist, name='blacklist'),
    path('company_reg', views.company_reg, name='company_reg'),
    path('company_update/<id>', views.company_update, name='company_update'),
    path('company/<slug>', views.company, name='company'),




]
