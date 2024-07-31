from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from .models import *

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'shared/index.html')







