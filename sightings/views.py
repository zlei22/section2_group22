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


def add(request,Unique_Squirrel_Id=None):
    if request.method=="POST":
        print(request.POST)
        data=request.POST
        ret=Sightings.objects.create(Unique_Squirrel_Id='123',longitude=data['longitutde'])
        if ret:
            return HttpResponse('Your answer has been recorded successfully')
        else:
            return HttpResponse("Your answer hasn't been recorded")
