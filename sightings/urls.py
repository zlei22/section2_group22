from django.urls import path
from sightings.views import *

urlpatterns = [
    path('', index, name='sightings_list'),
    path('<str:uid>/',details,name='sighting_uid'),
    path('add/',add,name='add'),

]
