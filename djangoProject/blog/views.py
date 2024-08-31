from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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
    