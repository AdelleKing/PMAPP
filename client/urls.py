from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='client'),
    path('accounts/login/', TenantLoginView.as_view(), name='tenant_login'),
]

