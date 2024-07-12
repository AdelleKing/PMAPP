
from django.contrib import admin
from django.urls import path
from .views import *


app_name="client_tenant"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='home'),
    path("index", index, name='index'),
    path('projectdetails/<int:task_id>/', projectdetails, name='projectdetails'),
    path('createcomment/<int:task_id>/', createcomment, name='createcomment'),
    path('deletecomment/<int:comment_id>/<int:task_id>/', deletecomment, name='deletecomment'),
    path('editcomment/<int:comment_id>/<int:task_id>/', editcomment, name='editcomment'),





    
]
