from django import forms
from .models import *



class CreateAdTextPostForm(forms.ModelForm):

    class Meta:
        model = AdTextPost
        fields = ('name', 'image', 'short_description', 'description')


class UpdateAdTextPostForm(forms.ModelForm):
    class Meta:
        model = AdTextPost
        fields = ('name', 'image', 'short_description', 'description')

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