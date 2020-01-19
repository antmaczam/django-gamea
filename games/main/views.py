from django.shortcuts import render
from main.models import Game

# Create your views here.

def inicio(request):
    games = Game.objects.all()
    return render(request,'index.html', {'games':games})

def games(request):
    games = Game.objects.all()
    text = ''
    return render(request,'games.html',{'games':games,'text':text})

def priceAsc(request):
    games = Game.objects.all().order_by('price').reverse()
    text = 'ordenados por precio ascendente'
    return render(request,'games.html',{'games':games,'text':text})

def priceDesc(request):
    games = Game.objects.all().order_by('price')
    text = 'ordenados por precio descendente'
    return render(request,'games.html',{'games':games,'text':text})