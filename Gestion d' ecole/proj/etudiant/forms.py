from django import forms
from .models import etud
from classe.models import classe

class etudRegistration(forms.ModelForm):
    classe = forms.ModelChoiceField(queryset=classe.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = etud
        fields = ['code', 'name', 'prenom', 'N_Tel', 'classe']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'N_Tel': forms.TextInput(attrs={'class': 'form-control'}),
             
            
        }

