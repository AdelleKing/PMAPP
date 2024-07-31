from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from client.models import *
from .forms import TenantLoginView


def public_index(request):
    return render(request, "public/public_index.html")


def about(request):
    return render(request, "public/about.html")

def login(request):
    form = TenantLoginView()
    return render(request, "public/login.html", {"form": form})

def login_view(request): 

    if request.method == 'POST':
        form = TenantLoginView(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            email_domain = username.split('@')[1]
            print(email_domain)
            tenant_name = email_domain.split('.')[0]
            print(tenant_name)
            tenant = Client.objects.get(name=tenant_name)
            print(tenant)
        except (Client.DoesNotExist, IndexError):
            return render(request, 'public/login.html', {'form':form, 'error': 'Invalid tenant'})

        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")
        if user is not None and user.tenant == tenant:
            login(request, user)
            return redirect(reverse('client_tenant:home'))
        else:
            return render(request, 'public/login.html', {'form':form, 'error': 'Invalid login credentials'})
    else:
        form=TenantLoginView()
        return render(request, 'public/login.html',{'form':form})