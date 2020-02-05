

from django.urls import path
from . import views

urlpatterns = [
    path('news/all', views.news_all, name='news_all'),
    path('news/<slug>', views.news, name='news'),



]
