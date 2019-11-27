from django.shortcuts import render
from .models import Squirrel


def index(request):
    squirrel=Squirrel.objects.all()
    context={'sightings':squirrel,} 
    return render(request,"sightings/index.html",context)


def details(request,uid=None):
    sighting=Squirrel.objects.get(uid)
    context={'sighting':squirrel,}
    return render(request,"sightings/details.html",context)
