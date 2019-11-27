from django.shortcuts import render


from .models import Squirrel

# Create your views here.

def index(request):
    latitude = Squirrel.objects.all().values_list('Latitude')
    longitude = Squirrel.objects.all().values_list('Longitude')
    context = {'Latitude':latitude,
            'Longitude':longitude}
    return render(request,'map/squirrels_tracker_map.html',context)
