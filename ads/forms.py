from django import forms
from .models import *



class CreateAdTextPostForm(forms.ModelForm):

    class Meta:
        model = AdTextPost
        fields = ('name',
                  'image',
                  'short_description',
                  'description')

class UpdateAdTextPostForm(forms.ModelForm):
    class Meta:
        model = AdTextPost
        fields = ('name',
                  'image',
                  'short_description',
                  'description')

class CreateAdVideoPostForm(forms.ModelForm):
    class Meta:
        model = AdVideoPost
        fields = ('name',
                  'image',
                  'video_link',
                  'short_description',
                  'description')

class UpdateAdViodePostForm(forms.ModelForm):
    class Meta:
        model = AdVideoPost
        fields = ('name',
                  'image',
                  'video_link',
                  'short_description',
                  'description')

  #  name
  #  author
  #  image
  #  video_link
  #  short_description
  #  description