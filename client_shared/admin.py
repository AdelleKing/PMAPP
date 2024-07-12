from django.contrib import admin

from client_shared.models import ProjectStage

@admin.register(ProjectStage)
class ProjectStageAdmin(admin.ModelAdmin):
    list_display = ("name",)
