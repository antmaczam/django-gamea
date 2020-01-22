from django.shortcuts import render
from main.models import Game
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from main.populate import extraerDatosURL

# Create your views here.

def inicio(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct()
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'index.html', {'games':games, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def games(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct()
    text = ''
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def priceAsc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('price').reverse()
    text = 'ordenados por precio ascendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def priceDesc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('price')
    text = 'ordenados por precio descendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def commentsAsc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('comments').reverse()
    text = 'ordenados por  numero de comentarios ascendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def commentsDesc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('comments')
    text = 'ordenados  por   numero  de  comentarios descendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def rateAsc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('rate').reverse().distinct()
    text = 'ordenados por valoracion ascendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def rateDesc(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().distinct().order_by('rate')
    text = 'ordenados por  valoracion descendente'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def topComments(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('comments').reverse()[:5]
    text = 'Top 5 numero de comentarios'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def topRate(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('rate').reverse()[:5]
    text = 'Top 5 numero de valoraciones'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def topPrice(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().order_by('price')[:5]
    text = 'Top 5 juegos  baratos'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def populate(request):
    extraerDatosURL()
    games = Game.objects.all()
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'index.html',{'games':games, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})
    
def pcGames(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().filter(plataform='PC')
    text = 'PC'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def xboxGames(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().filter(plataform__contains='xbox')
    text = 'XBox'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def psxGames(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().filter(plataform__contains='ps')
    text = 'PSX'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def nintendoGames(request):
    games = Game.objects.values('title','price','gamePrice','category','picture').distinct().filter(plataform__contains='Nintendo')
    text = 'Nintendo'
    if(len(topGames())>0):
        picture1 = topGames()[0].picture
        picture2 = topGames()[1].picture
        picture3 = topGames()[2].picture
    else:
        picture1 = ''
        picture2 = ''
        picture3 = ''
    return render(request,'games.html',{'games':games,'text':text, 'picture1':picture1, 'picture2':picture2, 'picture3':picture3})

def topGames():
    games = Game.objects.all().order_by('price')[:5]
    return games