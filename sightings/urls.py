from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sightings_list'),
    path('<str:uid>/',details,name='sightings_uid'),
    path('add/',add,name='add'),

]
