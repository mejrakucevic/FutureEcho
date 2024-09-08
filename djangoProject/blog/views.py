from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def letters(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/letters.html', context)

def about(request):
    return HttpResponse("<h1>Aloha 2</h1>")
    