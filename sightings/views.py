from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from map.models import Squirrel

def index(request):
    #text = ''
    #sightings=Sighting.objects.all()
    #for sighting in sightings:
     #   text += "Squirrel ID: %s<br>" %(sighting.uid)
    # return HttpResponse("This is a list of sightings.")
    #return HttpResponse(text)
    sightings=Squirrel.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)
    

def uid(request,uid):
    sighting=Sighting.objects.get(uid=uid)
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
            'Sighting': sightings,
    }
    return render(request,"sightings/stats.html",context)
