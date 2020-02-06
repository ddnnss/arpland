from django.shortcuts import render
from .models import *

def news_all(request):
    all_news = BlogPost.objects.all().filter(is_active=True)
    return render(request, 'page/posts.html', locals())

def news(request,slug):
    post = BlogPost.objects.get(name_slug=slug)
    all_news = BlogPost.objects.all().filter(is_active=True).exclude(id=post.id)
    post.views += 1
    post.save()
    return render(request, 'page/post.html', locals())