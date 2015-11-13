
from django.conf.urls import patterns, url
from station import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='station'),    
    url(r'^view/(?P<station_id>\w+)/', views.view_station, name='view_station'),
    url(r'^(?P<station_id>\w+)/values/add/', views.add_values, name='add_values'),
    url(r'^new/', views.new_station, name='new_station'),
)


