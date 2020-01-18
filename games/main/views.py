from django.shortcuts import render
from main.models import Game

# Create your views here.

def inicio(request):
    games = Game.objects.all()
    return render(request,'index.html', {'games':games})

def games(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})