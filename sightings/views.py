from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

def index(request):
    sightings=Sighting.objects.all()
    context={
        'sightings': sightings,
    }
    return render(request,"sightings/index.html",context)

def uid(request,uid=None):
    sighting=Sighting.objects.get(uid)
    context={
        'sighting': sighting,
    }
    return render(request,"sightings/uid.html",context)

def add(request,uid=None):
    if request.method=="POST":
        print(request.POST)
        data=request.POST
    context={
        'sighting': sightings,
    }
    return render(request,"sightings/add.html",context)

def stats(request):
    sightings=Sighting.objects.all()
    context={
        'sighting': sightings,
    }
    return render(request,"sightings/stats.html",context)
