from django.core import validators
from django import forms
from django.forms import fields
from .models import classe

class classeregistration(forms.ModelForm ):
 class Meta:
     model=classe
     fields=['name']
     widgets={
         'name': forms.TextInput(attrs={'class':'form-control'}),
         
         
     }