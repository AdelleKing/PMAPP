
from django.contrib import admin
from django.urls import path, include
from .views import *
from .forms import *
from django.conf import settings
from django.conf.urls.static import static



app_name="public"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", public_index, name='public_index'),
    path("about", about, name='about'),
    path("accounts/", include('allauth.urls')),
    path('login', login, name='login'),
    path('tenantlogin', login_view, name='tenantlogin'),
    path('client_tenant/', include(('client_tenant.urls', 'client_tenant'), namespace='client_tenant')),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
