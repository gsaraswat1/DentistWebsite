from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('contact.html', views.contact,name="contact"),
    path('pricing.html', views.pricing,name="pricing"),
    path('service.html', views.servicing,name="service"),
    path('blog.html', views.blog,name="blog"),
    path('blog-details.html', views.blog_details,name="blog-details"),
    path('about.html', views.about,name="about"),
    path('appointment.html', views.appointment,name="appointment"),
]
