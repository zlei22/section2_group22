from django.shortcuts import render
#from django.template import loader
from sightings.models import Sighting

# Create your views here.

def index(request):
    squirrels_x = Sighting.objects.all().values_list('longitude')
    squirrels_y = Sighting.objects.all().values_list('latitude')
    context = {'longitude':squirrels_x,
            'latitude':squirrels_y}
    #template = loader.get_template('map.html')
    #return HttpResponse(template.render(context, request))
    return render(request,'map/squirrel_tracker_map.html',context)

# test
