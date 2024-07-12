# forms.py
from django import forms

class TenantLoginForm(forms.Form):
    tenant_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
