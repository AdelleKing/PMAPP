from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render



def public_index(request):
    return render(request, "public/public_index.html")


def about(request):
    return render(request, "public/about.html")

