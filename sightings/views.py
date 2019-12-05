from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import Avg, Max, Min, Count

from .models import Sighting
from .form import SquirrelForm

def index(request):
    sightings=Sighting.objects.all()
    context={
        'sightings': sightings,
    }
    return render(request,"sightings/index.html",context)


def uid(request, uid):
    sighting = Sighting.objects.get(uid=uid)
    # sighting = Sighting.objects.get(uid=uid)
    # sighting = Sighting.objects.all()
    # if request.method == "POST":
        # sighting.shift = request.POST['sighting.shift']
        # sighting.save()
        # return redirect('sightings:uid')
    # elif request.method == "DELETE":
        # sighting.delete()
        # return redirect('sightings:index')
    # else:
    # context={
        # 'sighting': sighting,
    #}
    # return render(request,'sightings/uid.html',context)
    return HttpResponse(sighting)


def edit(request, uid):
    sighting = Sighting.objects.get(uid=uid)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{sighting.uid}')
    else:
        form = SquirrelForm(instance=sighting)
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)


def delete(request, uid):
    sighting = Sighting.objects.get(uid=uid)
    sighting.delete()
    return redirect(f'/sightings')
    # return render(reqest, 'sighting/edit.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)


def stats(request):
    sightings = Sighting.objects.all()
    totalnumber = Sighting.objects.count()
    stats_lat = sightings.aggregate(min_lat = Min('latitude'), max_lat = Max('latitude'), avg_lat = Avg('latitude'))
    stats_long = sightings.aggregate(min_long = Min('longitude'), max_long = Max('longitude'), avg_long = Avg('longitude'))
    adult_count = Sighting.objects.filter(age='Adult').count()
    juv_count = Sighting.objects.filter(age='Juvenile').count()
    adult = round(adult_count / totalnumber * 100)
    juvenile = round(juv_count/ totalnumber * 100)
    gray_count = Sighting.objects.filter(color = 'Gray').count()
    black_count = Sighting.objects.filter(color = 'Black').count()
    cin_count = Sighting.objects.filter(color = 'Cinnamon').count()
    gray = round (gray_count / totalnumber * 100)
    black = round (black_count/totalnumber * 100)
    cinnamon = round (cin_count / totalnumber *100)
    running = Sighting.objects.filter(running=True).count()
    not_running = Sighting.objects.filter(running=False).count()

    context={
        'sightings': sightings,
        'totalnumber':totalnumber,
        'stats_lat':stats_lat,
        'stats_long':stats_long,
        'adult':adult,
        'juvenile':juvenile,
        'gray':gray,
        'black':black,
        'cinnamon':cinnamon,
        'running':running,
        'not_running':not_running,


    }
    return render(request,"sightings/stats.html",context)
