from django.shortcuts import render


from .models import Squirrel

# Create your views here.

def index(request):
    squirrels_tracker_latitude = Squirrel.objects.all().values_list('latitude')
    squirrels_tracker_longitude = Squirrel.objects.all().values_list('longitude')
    context = {'latitude':squirrels_tracker_latitude,
            'longitude':squirrels_tracker_longitude}
    return render(request,'map/squirrel_tracker_map.html',context)


# test
