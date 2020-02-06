from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2','organization_name' )
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
                  'avatar',
                  'organization_site',
                  'organization_address',
                  'organization_description',
                  'organization_avatar',
                  'organization_vk',
                  'organization_inst',
                  'organization_yt',
                  'organization_ok',)

        error_messages = {
             'email': {
                 'unique': "Указанный адрес уже кем-то используется",
             },}


#     name
#     phone
#     avatar
#     organization_name
#     organization_site
#     organization_address
#     organization_description
#     organization_avatar
#     organization_vk
#     organization_fb
#     organization_inst
#     organization_yt
#     organization_ok