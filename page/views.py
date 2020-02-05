from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from blog.models import *
from customuser.forms import *






def index(request):
    try:
        latest_news = BlogPost.objects.all().order_by('-created_at')
    except:
        latest_news = None
    return render(request, 'page/index.html', locals())


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