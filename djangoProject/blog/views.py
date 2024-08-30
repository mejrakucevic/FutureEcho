from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Mejra K',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started..In this Python Django Tutorial, we will be learning how .',
        'datePosted': '28.4.2024'
    },
    
        {
        'author': 'Lottie M',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
        
    {
        'author': 'Natalie S',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
    
     {
        'author': 'Mejra',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
     
    {
        'author': 'Mejra',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
    
     {
        'author': 'Mejra',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
     
      {
        'author': 'Mejra',
        'title': 'Letter 1',
        'content': 'In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. Well also see how we can pass variables to our templates as context. Lets get started...In this Python Django Tutorial, we will be learning how ',
        'datePosted': '28.4.2024'
    },
    
]


def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def letters(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/letters.html', context)

def about(request):
    return HttpResponse("<h1>Aloha 2</h1>")
    