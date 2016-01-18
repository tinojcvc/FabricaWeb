
from django.shortcuts import render
from django.http import HttpResponse

from appmobile.models import MobileDevice
from util.utils import get_pagination

from FabricaWeb.decorators import login_required

import datetime

@login_required
def index(request):
    list_msg = MobileDevice.objects.all() #(is_read=False).order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render(request, 'appmobile/messages.html',
                  {'messages': messages, 'size': len(list_msg), 'home': True})

@login_required
def view_message(request, message_id):
    message = MobileDevice.objects.get(id=message_id)
    #message.update(is_read=True)

    list_content = MobileDevice.objects.filter(id=message_id)
    #phone_number = WhatsappReceived.objects.get(id=message_id)
    return render(request, 'appmobile/view_message.html',
                  {'list_content': list_content,})

def services(request):
    if request.GET.get('photo') and request.GET.get('imei'):
        photo = request.GET['photo']
        imei_device = request.GET['imei']

        if request.GET.get('latitude'):
            try:
                latitude = request.GET['latitude']
            except Exception:
                latitude = ""

        if request.GET.get('longitude'):
            try:
                longitude = request.GET['longitude']
            except Exception:
                longitude = ""
        if request.GET.get('altitude'):
            try:
                altitude = request.GET['altitude']
            except Exception:
                altitude = ""
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

