from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

@login_required
def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

@login_required
def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

