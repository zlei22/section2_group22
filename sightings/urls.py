from django.urls import path
from sightings import views
from sightings.views import *

urlpatterns = [
    path('', views.index),
    path('stats', stats, name='General Statistics'),
    path('<str:uid>', uid, name='Specific Information'),
    path('add', add, name='Add Sightings'),
]
