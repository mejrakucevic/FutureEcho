from django.urls import path 
from . import views



urlpatterns = [
    path('', views.home, name='blog-home'),
    
    path('contact/', views.contact, name='blog-contact'),
    path('letters/', views.letters, name='blog-letters'),
    
]
