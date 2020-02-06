

from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.news_all, name='news_all'),
    path('<slug>/', views.news, name='news'),



]
