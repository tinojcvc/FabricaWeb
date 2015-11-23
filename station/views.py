from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from datetime import datetime
from station.models import Station, StationValues

from station.serializers import StationSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


def index(request):
    stations = Station.objects
    return render_to_response('index.html', {'stations': stations},
                              context_instance=RequestContext(request))

def services(request, num_station):
    print '------------------------'
    print num_station
    print '------------------------'
    station = Station.objects.get(num_station=num_station)
    ss = StationSerializer(station)
    render = JSONRenderer().render(ss.data)
#    stream = BytesIO(render)
#    data = JSONParser().parse(stream)
#    print data

    return HttpResponse(render)

def new_station(request):
    if request.method == 'POST':
        # save new post
        name = request.POST['name_station']
        num_station = request.POST['num_station']
        date_creation = datetime.now()

        station = Station(name=name, num_station=num_station, date_creation=date_creation)
        station.save()

        stations = Station.objects
        return HttpResponseRedirect('/')
    else:
        return render(request, 'new_station.html')

def view_station(request, station_id):
    station = Station.objects.get(id=station_id)
    list_values_station = StationValues.objects.filter(station=station)

    return render_to_response('station.html', {'station': station,
                                               'list_values': list_values_station},
                              context_instance=RequestContext(request))

def add_values(request, station_id):
    station = Station.objects.get(id=station_id)

    if request.method == 'POST':
        pressure = request.POST['pressure']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        wind_speed = request.POST['wind_speed']
        time = datetime.now()

        sv = StationValues(station=station,
                           pressure=pressure,
                           temperature=temperature,
                           humidity=humidity,
                           wind_speed=wind_speed,
                           time=time)
        sv.save()
        list_values_station = StationValues.objects.filter(station=station)
        return render(request, 'station.html', {'station': station,
                                                'list_values': list_values_station})
    else:
        return render_to_response('add_values.html', {'station': station},
                                  context_instance=RequestContext(request))

