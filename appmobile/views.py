
from django.shortcuts import render_to_response
from django.http import HttpResponse

from appmobile.models import MobileDevice
from util.utils import get_pagination

import datetime

def index(request):
    list_msg = MobileDevice.objects.filter(is_read=False).order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render_to_response('appmobile/messages.html',
                              {'messages': messages,
                               'size': len(list_msg),
                               'home': True})

def services(request):
    if request.GET.get('photo') and request.GET.get('imei'):
        photo = request.GET['photo']
        imei_device = request.GET['imei']

        if request.GET.get('latitude'):
            try:
                latitude = float(request.GET['latitude'])
            except ValueError:
                latitude = 0.0
        if request.GET.get('longitude'):
            try:
                longitude = float(request.GET['longitude'])
            except ValueError:
                longitude = 0.0
        if request.GET.get('altitude'):
            try:
                altitude = float(request.GET['altitude'])
            except ValueError:
                altitude = 0.0
        if request.GET.get('orientation'):
            try:
                orientation = float(request.GET['orientation'])
            except ValueError:
                orientation = 0.0
        if request.GET.get('speed'):
            try:
                speed = str(request.GET['speed'])
            except ValueError:
                speed = ''
        if request.GET.get('message'):
            try:
                message = request.GET['message']
            except Exception:
                message = ''
        if request.GET.get('number'):
            number_phone = request.GET['number']
        else:
            number_phone = None

        print '-------------------'
        print photo
        print '-------------------'
        mobile_device = MobileDevice(photo=photo,
                                    latitude=latitude,
                                    longitude=longitude,
                                    altitude=altitude,
                                    orientation=orientation,
                                    speed=speed,
                                    imei_device=imei_device,
                                    number_phone=number_phone,
                                    message=message,
                                    date_creation=datetime.datetime.now())
        mobile_device.save()

        return HttpResponse('OK')
    else:
        return HttpResponse('Datos invalidos')

