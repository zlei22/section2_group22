from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting


def index(request):
    sightings=Sighting.objects.all()
    context={
        'sightings': sightings,
    }
    return render(request,"sightings/index.html",context)


def uid(request,uid):
    sighting=Sighting.objects.get(uid=uid)
    if request.method=="POST":
        sighting.shift=request.POST['sighting.shift']
        sighting.save()
        return redirect('sightings:uid')
    elif request.method=="DELETE":
        sighting.delete()
        return redirect('sightings:index')
    else:
        context={
            'sighting': sighting,
        }
        return render(request,"sightings/uid.html",context)


def add(request):
    if request.method=="POST":
        uid = request.POST.get('uid')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        shift = request.POST.get('shift')
        date = request.POST.get('date')
        age = request.POST.get('age')
        color = request.POST.get('color')
        loc = request.POST.get('loc')
        specific_loc = request.POST.get('specific_loc')
        running = request.POST.get('running')
        chasing = request.POST.get('chasing')
        climbing = request.POST.get('climbing')
        eating = request.POST.get('eating')
        foraging = request.POST.get('foraging')
        other_act = request.POST.get('other_act')
        kuks = request.POST.get('kuks')
        quaas = request.POST.get('quaas')
        moans = request.POST.get('moans')
        tail_flags = request.POST.get('tail_flags')
        tail_twitches = request.POST.get('tail_twitches')
        approaches = request.POST.get('approaches')
        indifferent = request.POST.get('indifferent')
        runs_from = request.POST.get('runs_from')

        sighting=Sighting.objects.create(uid=uid, latitude=latitude, longitude=longitude,
                shift=shift, date=date, age=age, color=color, loc=loc, specific_loc=specific_loc,
                running=running, chasing=chasing, climbing=climbing, eating=eating, foraging=foraging,
                other_act=other_act, kuks=kuks, quaas=quaas, moans=moans, tail_flags=tail_flags,
                tail_twitches=tail_twitches, approaches=approaches, indifferent=indifferent,
                runs_from=runs_from)
        sighting.save()
        return redirect('sightings:index')
    return render(request,"sightings/add.html",context)


def stats(request):
    sightings=Sighting.objects.all()
    totalnumber=Sighting.object.count()
    stats_lat = Sightings.aggregate(min_lat = Min('latitude'), max_lat = Max('latitude'), avg_lat = Avg('latitude'))
    stats_long = Sightings.aggregate(min_long = Min('longitude'), max_lat = Max('longitude'), avg_lat = Avg('longitude'))
    adult_count = Sighting.objects.filter(age='Adult').count()
    juv_count = Sighting.objects.filter(age='Juvenile').count()
    adult = round(adult_count / totalnumber * 100)
    juvenile = round(juv_count/ totalnumber * 100)
    gray_count = Sighting.objects.filter(color = 'Gray').count()
    black_count = Sighting.objects.filter(color = 'black').count()
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
        'gray':gray
        'balck':black
        'cinnamon':cinnamon
        'running':running
        'not_running':not_running


    }
    return render(request,"sightings/stats.html",context)
