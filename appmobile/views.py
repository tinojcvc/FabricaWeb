from django.shortcuts import render
from django.http import HttpResponse

from appmobile.models import MobileDevice

import datetime

# Create your views here.

def services(request):
    if request.GET.get('photo'):
        photo = request.GET['photo']
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        altitude = request.GET['altitude']
        orientation = request.GET['orientation']
        speed = request.GET['speed']
        imei_device = request.GET['imei']
        if request.GET.get('phone'):
            number_phone = request.GET['phone']
        else:
            number_phone = None

        mobile_device = MobileDevice(photo=photo,
                                     latitude=latitude,
                                     longitude=longitude,
                                     altitude=altitude,
                                     orientation=orientation,
                                     speed=speed,
                                     imei_device=imei_device,
                                     number_phone=number_phone,
                                     date_creation=datetime.datetime.now())
        mobile_device.save()

        return HttpResponse('OK')
    else:
        HttpResponse('Datos invalidos')

