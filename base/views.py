from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def experience(request):
    return render(request, 'main/experience.html')
