from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def experience(request):
    return render(request, 'main/experience.html')
