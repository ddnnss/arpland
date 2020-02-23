from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2','name',)
        error_messages = {
            'email': {
                'unique': "Указанный адрес уже кем-то используется",
            }, }

class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User

        fields = ('email',
                  'name',
                  'phone',
                  'avatar',)

        error_messages = {
             'email': {
                 'unique': "Указанный адрес уже кем-то используется",
             },}

class CompanyCreate(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name',
                  'site',
                  'address',
                  'description',
                  'avatar',
                  'vk',
                  'fb',
                  'inst',
                  'yt',
                  'ok',)

class CompanyUpdate(forms.ModelForm):
   
    class Meta:
        model = Company

        fields = ('name',
                  'site',
                  'address',
                  'description',
                  'avatar',
                  'vk',
                  'fb',
                  'inst',
                  'yt',)






#     
#     name
#     site
#     address
#     description
#     avatar
#     vk
#     fb
#     inst
#     yt
#     ok