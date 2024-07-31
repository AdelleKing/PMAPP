from django.contrib import admin
from client_tenant.models import Project
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)



