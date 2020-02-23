from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from blog.models import *
from customuser.forms import *
from ads.forms import *
from .models import *
from customuser.forms import UpdateForm
from ads.models import *
from .forms import *





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
    all_companies = Company.objects.filter(user=request.user)

    return render(request, 'page/lk.html', locals())

def about(request):
    aboutInfo = Contact.objects.first()
    return render(request, 'page/about.html', locals())

def contact(request):
    if request.POST:
        Callback.objects.create(name=request.POST.get('name'),
                                email=request.POST.get('email'),
                                text=request.POST.get('text'))
    contact = Contact.objects.first()
    return render(request, 'page/contact.html', locals())

def companies(request):
    all_company = Company.objects.all()
    return render(request, 'page/all_orgs.html', locals())

def company_info(request,slug):
    company = Company.objects.get(name_slug=slug)
    all_text_ad = AdTextPost.objects.filter(author=company)
    all_video_ad = AdVideoPost.objects.filter(author=company)
    return render(request, 'page/org.html', locals())

def profile_edit(request):
    form = UpdateForm(instance=request.user)
    return render(request, 'page/lk-edit.html', locals())

def profile_add_text(request,id):
    if id != '0':
        company = Company.objects.get(id=id)
    if request.POST:
        data = request.POST.copy()
        form = CreateAdTextPostForm(request.POST, request.FILES)

        print(form.errors)

        if not form.errors:
            newAd = form.save(commit=False)
            newAd.author_id = request.POST.get('author')
            newAd.save()
            print(newAd.id)
            return HttpResponseRedirect("/profile")
        else:
            print(form.errors)
            data, errors = {}, {}
            messages.success(request, form.errors)
            return HttpResponseRedirect("/profile-add-text")
    form =CreateAdTextPostForm()

    return render(request, 'page/lk-add-text-ad.html', locals())

def profile_add_video(request,id):
    if id != '0':
        company = Company.objects.get(id=id)
    if request.POST:
        data = request.POST.copy()
        form = CreateAdVideoPostForm(request.POST, request.FILES)

        print(form.errors)

        if not form.errors:
            newAd = form.save(commit=False)
            newAd.author_id = request.POST.get('author')
            newAd.save()
            print(newAd.id)
            return HttpResponseRedirect("/profile")
        else:
            print(form.errors)
            form = CreateAdVideoPostForm()
            data, errors = {}, {}
            messages.success(request, form.errors)
            return HttpResponseRedirect("/profile-add-video")
    form = CreateAdVideoPostForm()
    return render(request, 'page/lk-add-video-ad.html', locals())

def profile_add_bl(request):
    if request.POST:
        data = request.POST.copy()
        form = CreateBL(request.POST, request.FILES)

        print(form.errors)

        if not form.errors:
            newAd = form.save(commit=False)
            newAd.author = request.user
            newAd.save()
            print(newAd.id)
            return HttpResponseRedirect("/profile")
        else:
            print(form.errors)
            form = CreateBL()
            data, errors = {}, {}
            messages.success(request, form.errors)
            return HttpResponseRedirect("/profile-add-bl")
    form = CreateBL()
    return render(request, 'page/lk-add-bl.html', locals())
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
            return HttpResponseRedirect("/profile")
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
            return HttpResponseRedirect("/profile")
        else:
            messages.success(request, 'Проверьте введенные данные')
            return HttpResponseRedirect('/login')
    return render(request, 'page/login.html', locals())


def blacklist_all(request):
    blAll = BlackList.objects.filter(isModerated=True)
    return render(request, 'page/bl-all.html', locals())

def blacklist(request,slug):
    blItem = BlackList.objects.get(name_slug=slug)
    return render(request, 'page/bl.html', locals())


def company_reg(request):
    form = CompanyCreate()
    if request.POST:
        print(request.POST)
        form = CompanyCreate(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()

            return HttpResponseRedirect('/profile')
        else:
            form = UpdateForm()
            messages.success(request, form.errors)
        return HttpResponseRedirect("/company_reg")
    return render(request, 'page/company_add.html', locals())

def company_update(request,id):
    company=Company.objects.get(id=id)
    form = CompanyUpdate(instance=company)
    if request.POST:
        print(request.POST)
        form = CompanyUpdate(request.POST, request.FILES,instance=company)
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            form = CompanyUpdate(instance=company)
            messages.success(request, form.errors)
        return HttpResponseRedirect("/company_reg")

    return render(request, 'page/company-edit.html', locals())
def company(request,slug):
    company = Company.objects.get(name_slug=slug)
    all_text_ad = AdTextPost.objects.filter(author=company)
    all_video_ad = AdVideoPost.objects.filter(author=company)
    return render(request, 'page/company.html', locals())

def tender(request):
    return render(request, 'page/investor.html', locals())
