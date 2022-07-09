from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    catas = Cat.objects.all()
    draw = Pics.objects.filter(cat__id=4)
    paint = Pics.objects.filter(cat__id=5)
    comic = Pics.objects.filter(cat__id=6)
    context = {
        'cat':catas,
        'draw':draw,
        'paint':paint,
        'comic':comic,
    }
    return render(request, 'album/index.html', context)

def dark(request):
    return render(request,'dark/index.html')

def album(request,pk):
    Draw = Pics.objects.filter(cat__id=pk)
    context = {
        "album":Draw
    }
    return render(request,'album/album.html',context)