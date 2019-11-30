from django.urls import path
from sightings import views
from sightings.views import *

urlpatterns = [
    # List of Sightings: /sightings
    path('', views.index, name='index'),

    # Update and Delete: /sightings/<uid>
    path('<str:uid>', uid, name='update'),

    # Add New Sightings: /sightings/add
    path('add', add, name='add'),

    # Check Up Statistics: /sightings/stats
    path('stats', stats, name='stats'),
 ]
