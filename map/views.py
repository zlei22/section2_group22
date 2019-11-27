from django.shortcuts import render


from .models import Squirrel

# Create your views here.

def index(request):
    squirrels_tracker_latitude = Squirrel.objects.all().values_list('Latitude')
    squirrels_tracker_longitude = Squirrel.objects.all().values_list('Longitude')
    context = {'squirrels_latitude':squirrels_tracker_latitude,
            'squirrels_longitude':squirrels_tracker_longitude}
    return render(request,'map/squirrels_tracker_map.html',context)


# test
