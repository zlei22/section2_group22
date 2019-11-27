from django.shortcuts import render


from .models import Squirrels

# Create your views here.

def index(request):
    squirrels_tracker_latitude = Squirrels.objects.all().values_list('latitude')
    squirrels_tracker_longitude = Squirrels.objects.all().values_list('longitude')
    context = {'squirrels_latitude':squirrels_tracker_latitude,
            'squirrels_longitude':squirrels_tracker_longitude}
    return render(request,'map/squirrels_tracker_map.html',context)


# test
