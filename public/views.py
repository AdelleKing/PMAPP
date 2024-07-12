from django.shortcuts import render

def public_index(request):
    return render(request, "public/public_index.html")


def about(request):
    return render(request, "public/about.html")
