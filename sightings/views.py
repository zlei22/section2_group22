from django.shortcuts import render
from django.http import HttpResponse
from map.models import Squirrel

def index(request):
    text = ''
    sightings=Squirrel.objects.all()
    for sighting in sightings:
        text += sighting + '<This is a link.>'  + '\n'
    return HttpResponse("This is a list of sightings.")
   # return HttpResponse(text)

def uid(request,uid=None):
    sighting=Squirrel.objects.get(uid)
    context={
            'Sighting': sighting,
    }
    return render(request,"sightings/uid.html",context)

def add(request,uid=None):
    if request.method=="POST":
        print(request.POST)
        data=request.POST
    context={
            'Sighting': sightings,
    }
    return render(request,"sightings/add.html",context)

def stats(request):
    sightings=Squirrel.objects.all()
    context={
            'Sighting': sightings,
    }
    return render(request,"sightings/stats.html",context)
