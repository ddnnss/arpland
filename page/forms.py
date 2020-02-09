from django import forms
from .models import *



class CreateBL(forms.ModelForm):

    class Meta:
        model = BlackList
        fields = ('blackListType',
                  'name',
                  'contacts',
                  'why',
                  'moneyLost',
                  'profile',
                  'file',
                  'isAgreed',
                  )
