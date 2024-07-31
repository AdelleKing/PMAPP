# forms.py
from django import forms


class TenantLoginView(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
