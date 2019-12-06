from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),

    path('add', views.add),
    # url(r'^add$', views.add),

    path('stats', views.stats),
    # url(r'^stats$', views.stats),
    
    path('<str:squirrel_id>', views.details),
    # url(r'^<str:uid>$', views.uid),

    path('<str:squirrel_id>/edit', views.edit),

    path('<str:squirrel_id>/delete', views.delete)
 ]
