
from station import views

from django.conf.urls import url

urlpatterns = [
    url(r'^', views.index, name='station'),
    url(r'^services/(?P<num_station>\w+)/', views.services, name='services'),
    url(r'^view/(?P<station_id>\w+)/', views.view_station, name='view_station'),
    url(r'^(?P<station_id>\w+)/values/add/', views.add_values, name='add_values'),
    url(r'^new/', views.new_station, name='new_station'),
]


