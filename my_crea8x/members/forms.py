from django import forms
from .models import UserDetails

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    skills = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Comma-separated skills"}))

    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password', 'skills']
