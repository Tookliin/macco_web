from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('experience', views.experience, name="experience")
]
