
from wasend import YowsupSendStack
from wareceive import (YowsupReceiveStack,
                       MessageReceived,
                       MediaMessageReceived)
from models import WhatsappReceived
from utils import getMediaFromHttps

import datetime

def credential():
     return "59167479531", "kgWT7zbZhFxGEl/fJoVGwn/Kzbw="
<<<<<<< HEAD
=======

def saveWhatsapp(phone, type_message, message):
    dbphone = WhatsappReceived.objects.filter(phone=phone).order_by('-date_creation')
    len_dbphone = len(dbphone)
    if len_dbphone > 0:
        print '------------------'
        print 'El telefono existe'
        print '------------------'
        now = datetime.datetime.now()
        if dbphone[0].date_creation.date() == now.date() and now < (dbphone[0].date_creation + datetime.timedelta(minutes=30)):
            if type_message is not 'image':
                last_message = dbphone[0].message
                print '-----------------'
                print dbphone[0].date_creation.date()
                print 'mensaje anterior: ' + last_message
                print 'mensaje ultimo: ' + message
                print '-----------------'
                try:
                    current_message = last_message + ' ' + message
                    dbphone[0].update(message=current_message)
                except Exception as e:
                    print '******************'
                    print e
                    print '******************'
            else:
                if dbphone[0] is None:
                    try:
                        dbphone[0].update(image=getMediaFromHttps(message),
                                          is_complete=True)
                    except Exception as e:
                        print '******************'
                        print e
                        print '******************'
                else:
                    whatsapp = WhatsappReceived(phone=phone,
                                                message='',
                                                image=getMediaFromHttps(message),
                                                is_valid=False,
                                                is_complete=False,
                                                date_creation=datetime.datetime.now())
                    whatsapp.save()


        else:
            if type_message is 'image':
                whatsapp = WhatsappReceived(phone=phone,
                                            message='',
                                            image=getMediaFromHttps(message),
                                            is_valid=False,
                                            is_complete=False,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()
            else:
                whatsapp = WhatsappReceived(phone=phone,
                                            message=message,
                                            image=None,
                                            is_valid=False,
                                            is_complete=False,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()

    else:
        if type_message is 'text':
            whatsapp = WhatsappReceived(phone=phone,
                                        message=message,
                                        image=None,
                                        is_valid=True,
                                        is_complete=False,
                                        date_creation=datetime.datetime.now())
        else:
            whatsapp = WhatsappReceived(phone=phone,
                                        message='',
                                        image=getMediaFromHttps(message),
                                        is_valid=True,
                                        is_complete=False,
                                        date_creation=datetime.datetime.now())
        whatsapp.save()
>>>>>>> a0b07b208df350975545deee7736efde8ee8ab75

while True:
    try:
        stack=YowsupReceiveStack(credential())
        stack.start()
    except MediaMessageReceived as media_message:
        received = media_message.value
        phone = received[:11]
        media_list = media_message.getListMessage()
        print '++++++++++++++++++++++++++++++++++++++++'
        print 'Phone: ' + phone
        print 'Media URL: ' + media_list['url']
        print 'Type: ' + media_list['type']
        print '++++++++++++++++++++++++++++++++++++++++'

        saveWhatsapp(phone=phone,
                     type_message=media_list['type'],
                     message=media_list['url'])

    except MessageReceived as rcvd:
        received=rcvd.value
        phone = received[:11]
        message = received[11:]

        print '------------------------'
        print 'Phone: ' + phone
        print 'Message: ' + message
        print '------------------------'

        saveWhatsapp(phone=phone, type_message='text', message=message)
"""
        dbphone = WhatsappReceived.objects.filter(phone=phone).order_by('-date_creation')
        len_dbphone = len(dbphone)
        if len_dbphone > 0:
            print '------------------'
            print 'El telefono existe'
            print '------------------'
            now = datetime.datetime.now()
            if dbphone[0].date_creation.date() == now.date() and now < (dbphone[0].date_creation + datetime.timedelta(minutes=30)):
                last_message = dbphone[0].message
                print '-----------------'
                print dbphone[0].date_creation.date()
                print 'mensaje anterior: ' + last_message
                print 'mensaje ultimo: ' + message
                print '-----------------'
                try:
                    current_message = last_message + ' ' + message
                    dbphone[0].update(message=current_message)
                except Exception as e:
                    print '******************'
                    print e
                    print '******************'
            else:
                whatsapp = WhatsappReceived(phone=phone,
                                            message=message,
                                            image='asdf',
                                            is_valid=True,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()
        else:
            whatsapp = WhatsappReceived(phone=phone,
                                        message=message,
                                        image='asdf',
                                        is_valid=True,
                                        date_creation=datetime.datetime.now())
            whatsapp.save()
    """


