from django.urls import path
from django.conf.urls import url
from sightings import views
from sightings.views import *

urlpatterns = [
    # List of Sightings: /sightings
    path('', views.index, name='index'),

    # Update and Delete: /sightings/<uid>
    path('<str:uid>', views.uid, name='details'),
    # url(r'^<str:uid>$', views.uid),

    path('<str:uid>/edit', views.edit, name='edit'),

    # Add New Sightings: /sightings/add
    path('add', views.add, name='add'),
    # url(r'^add$', views.add),

    # Check Up Statistics: /sightings/stats
    path('stats', views.stats, name='stats'),
    # url(r'^stats$', views.stats),
 ]
