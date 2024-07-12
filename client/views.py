from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from .forms import TenantLoginForm
from .models import Client

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'shared/index.html')




class TenantLoginView(View):
    form_class = TenantLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            tenant_name = form.cleaned_data['tenant_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            tenant = Client.objects.get(name=tenant_name)
            user = authenticate(username=username, password=password, tenant=tenant)
            if user is not None:
                login(request, user)
                return redirect(f"http://{tenant.schema_name}.localhost:8000/dashboard/")
        return render(request, self.template_name, {'form': form, 'error': 'Invalid credentials'})



