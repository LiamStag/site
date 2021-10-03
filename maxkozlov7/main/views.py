from django.shortcuts import render
from main.models import *
#from django.http import HttpResponse

menu = ['About me', 'Portfolio', 'Price']

def index(request):
    posts = Video.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


