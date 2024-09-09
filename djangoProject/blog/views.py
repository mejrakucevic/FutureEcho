from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Game


def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def game_list(request):
    games = Game.objects.all()[:10]
    return render(request, 'blog/letters.html', {'games': games})

def about(request):
    return HttpResponse("<h1>Aloha 2</h1>")
    