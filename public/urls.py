
from django.contrib import admin
from django.urls import path, include
from .views import public_index, about
from django.conf import settings
from django.conf.urls.static import static


app_name="public"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", public_index, name='public_index'),
    path("about", about, name='about'),
    path("accounts/", include('allauth.urls')),

    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
