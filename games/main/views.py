from django.shortcuts import render
from main.models import Game
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from main.populate import extraerDatosURL

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

def commentsAsc(request):
    games = Game.objects.all().order_by('comments').reverse()
    text = 'ordenados por  numero de comentarios ascendente'
    return render(request,'games.html',{'games':games,'text':text})

def commentsDesc(request):
    games = Game.objects.all().order_by('comments')
    text = 'ordenados  por   numero  de  comentarios descendente'
    return render(request,'games.html',{'games':games,'text':text})

def rateAsc(request):
    games = Game.objects.all().order_by('rate').reverse()
    text = 'ordenados por valoracion ascendente'
    return render(request,'games.html',{'games':games,'text':text})

def rateDesc(request):
    games = Game.objects.all().order_by('rate')
    text = 'ordenados por  valoracion descendente'
    return render(request,'games.html',{'games':games,'text':text})

def topComments(request):
    games = Game.objects.all().order_by('comments').reverse()[:5]
    text = 'Top 5 numero de comentarios'
    return render(request,'games.html',{'games':games,'text':text})

def topRate(request):
    games = Game.objects.all().order_by('rate').reverse()[:5]
    text = 'Top 5 numero de valoraciones'
    return render(request,'games.html',{'games':games,'text':text})

def topPrice(request):
    games = Game.objects.all().order_by('price')[:5]
    text = 'Top 5 juegos  baratos'
    return render(request,'games.html',{'games':games,'text':text})

def populate(request):
    extraerDatosURL()
    games = Game.objects.all()
    return render(request,'index.html',{'games':games})
    
