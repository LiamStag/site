from django.shortcuts import render
from main.models import *
#from django.http import HttpResponse

menu = ['About me', 'Portfolio', 'Price']
contact = {'Instagram': 'https://www.instagram.com/maxkozlov7/', 'VKontakte': 'https://vk.com/maximkozlow7', 'YouTube': 'https://www.youtube.com/channel/UC4k8S3D6GnQibId4a9iKq6g'}

def index(request):
    posts = Video.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'contact': contact, 'title': 'Главная страница'})

def about(request):
    posts = Video.objects.all()
    return render(request, 'main/about.html', {'posts': posts, 'menu': menu, 'contact': contact, 'title': 'Обо мне'})


