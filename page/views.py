from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from blog.models import *
from customuser.forms import *
from .models import *
from customuser.forms import UpdateForm
from ads.models import *





def index(request):
    indexActive = True
    banners = Banner.objects.all()
    textAds = AdTextPost.objects.filter(is_published_at_index=True)
    videoAds = AdVideoPost.objects.filter(is_published_at_index=True)
    try:
        latest_news = BlogPost.objects.all().order_by('-created_at')
    except:
        latest_news = None
    return render(request, 'page/index.html', locals())


def profile(request):
    return render(request, 'page/lk.html', locals())

def about(request):
    return render(request, 'page/about.html', locals())

def contact(request):
    return render(request, 'page/contact.html', locals())

def companies(request):
    all_company = User.objects.all()
    return render(request, 'page/all_orgs.html', locals())

def company(request,slug):
    company = User.objects.get(organization_name_slug=slug)
    return render(request, 'page/org.html', locals())

def profile_edit(request):
    form = UpdateForm(instance=request.user)
    return render(request, 'page/lk-edit.html', locals())

def text_ads(request):
    all_text_ads = AdTextPost.objects.all()
    return render(request, 'page/text_ads.html', locals())

def text_ad(request,slug):
    textAd = AdTextPost.objects.get(name_slug=slug)
    commonAd = AdTextPost.objects.all()
    textAd.views += 1
    textAd.save()

    return render(request, 'page/text_ad.html', locals())
def video_ads(request):
    all_vide_ads = AdVideoPost.objects.all()
    return render(request, 'page/video_ads.html', locals())

def video_ad(request,slug):
    videoAd = AdVideoPost.objects.get(name_slug=slug)
    commonAd = AdVideoPost.objects.all()
    videoAd.views +=1
    videoAd.save()
    return render(request, 'page/video_ad.html', locals())

def registration(request):
    if request.POST:
        data = request.POST.copy()

        form = SignUpForm(data)

        if not form.errors:
            new_user = form.save(data)
            login(request, new_user)
            return HttpResponseRedirect("/lk")
        else:
            print(form.errors)
            data, errors = {}, {}
            messages.success(request, form.errors)
        return HttpResponseRedirect("/registration")

    form = SignUpForm()
    return render(request, 'page/register.html', locals())

def login_page(request):
    if request.POST:
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/lk")
        else:
            messages.success(request, 'Проверьте введенные данные')
            return HttpResponseRedirect('/login')
    return render(request, 'page/login.html', locals())