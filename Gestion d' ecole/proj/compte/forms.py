from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreerutilUsateur(UserCreationForm):
    Email=forms.EmailField
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','password1', 'password2']  # Include 'password1' and 'password2' fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add widget attributes for username, password1, and password2 fields
        for field_name in ['username','email' ,'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

