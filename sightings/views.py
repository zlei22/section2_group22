from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from map.models import Squirrel

def index(request):
<<<<<<< HEAD
    sightings=Sighting.objects.all()
    context={
        'sightings': sightings,
    }
    return render(request,"sightings/index.html",context)
    
>>>>>>> 8ba5d5d05ca71767436e540899f4ac87eae0f7bf

def uid(request,uid):
    sighting=Sighting.objects.get(uid=uid)
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

def delete(request,uid=None):
    sighting=squirrels.objects.get(uid=uid)
    if request.method=="POST":
        sighting.delete()
        return redirect('sightings:index')
    else:
        context={
            'Sighting': sightings,
    }
        return render(request,"sightings/delete.html",context)

def stats(request):
    sightings=Sighting.objects.all()
    context={
        'sighting': sightings,
    }
    return render(request,"sightings/stats.html",context)
