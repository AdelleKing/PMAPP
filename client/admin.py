from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from client.models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)



