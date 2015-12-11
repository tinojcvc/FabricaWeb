#!/home/cerrajero/Projects/hades-env/bin/python

from yowsup.layers.auth import AuthError

from wasend import YowsupSendStack
from wareceive import (YowsupReceiveStack,
                       MessageReceived,
                       MediaMessageReceived)
from models import WhatsappReceived
from utils import getMediaFromHttps
from thread import start_new_thread

import datetime
import time

def credential():
     return "591", ""

def anomaly_detector(phone, image, whatsapp):
    print 'PROCESANDO DEL TELEFONO: %s' % phone
    time.sleep(5)
    whatsapp.update(anomaly=True)
    #disanti_function()

def saveWhatsapp(phone, type_message, message):
    dbphone = WhatsappReceived.objects.filter(phone=phone).order_by('-date_creation')
    len_dbphone = len(dbphone)
    if len_dbphone > 0:
        print '------------------'
        print 'El telefono existe'
        print '------------------'
        now = datetime.datetime.now()
        if dbphone[0].date_creation.date() == now.date() and\
                now < (dbphone[0].date_creation\
                + datetime.timedelta(minutes=2)):
            if type_message is not 'image' and type_message is not 'video' and type_message is not 'audio':
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
                if type_message is 'image':
                    if not dbphone[0].image:
                        try:
                            print '**********************************'
                            print 'EN EL TRY PARA GUARDAR LA IMAGEN TELEFONO: ' + dbphone[0].phone
                            print '**********************************'
                            # TODO: la actualizacion del campo del imagen funciona
                            # desde el interprete, pero desde aqui no, al parecer
                            # es un bug o algo. Tendria que funcionar con:
                            #dbphone[0].image = getMediaFromHttps(message)
                            #dbphone[0].save()
                            #usando el update() sale el error de cadena invalida
                            messagedb = dbphone[0].message
                            dbphone[0].delete()
                            image_whatsapp = getMediaFromHttps(message)
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message=messagedb,
                                                        image=image_whatsapp,
                                                        is_complete=True,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                            try:
                                #ubal_value = anomaly_detector(image_whatsapp)
                                start_new_thread(anomaly_detector,(phone, image_whatsapp, whatsapp))
                            except:
                                print "ERROR: PROBLEMA CON EL THREAD"
                        except Exception as e:
                            print '******************'
                            print e
                            print '******************'
                    else:
                        if dbphone[0]:
                            image_whatsapp = getMediaFromHttps(message)
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message='',
                                                        image=image_whatsapp,
                                                        is_valid=False,
                                                        is_complete=False,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                            try:
                                #ubal_value = anomaly_detector(image_whatsapp)
                                start_new_thread(anomaly_detector,(phone, image_whatsapp, whatsapp))
                            except:
                                print "ERROR: PROBLEMA CON EL THREAD"

                elif type_message is 'audio':
                    if not dbphone[0].audio:
                        try:
                            print '**********************************'
                            print 'EN EL TRY PARA GUARDAR EL AUDIO DEL TELEFONO: ' + dbphone[0].phone
                            print '**********************************'
                            # TODO: la actualizacion del campo del imagen funciona
                            # desde el interprete, pero desde aqui no, al parecer
                            # es un bug o algo. Tendria que funcionar con:
                            #dbphone[0].image = getMediaFromHttps(message)
                            #dbphone[0].save()
                            #usando el update() sale el error de cadena invalida
                            messagedb = dbphone[0].message
                            dbphone[0].delete()
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message=messagedb,
                                                        audio=getMediaFromHttps(message),
                                                        is_complete=True,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                        except Exception as e:
                            print '******************'
                            print e
                            print '******************'
                    else:
                        if dbphone[0]:
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message='',
                                                        audio=getMediaFromHttps(message),
                                                        is_valid=False,
                                                        is_complete=False,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                elif type_message is 'video':
                    if not dbphone[0].video:
                        try:
                            print '**********************************'
                            print 'EN EL TRY PARA GUARDAR EL VIDEO DEL TELEFONO: ' + dbphone[0].phone
                            print '**********************************'
                            # TODO: la actualizacion del campo del imagen funciona
                            # desde el interprete, pero desde aqui no, al parecer
                            # es un bug o algo. Tendria que funcionar con:
                            #dbphone[0].image = getMediaFromHttps(message)
                            #dbphone[0].save()
                            #usando el update() sale el error de cadena invalida
                            messagedb = dbphone[0].message
                            dbphone[0].delete()
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message=messagedb,
                                                        video=getMediaFromHttps(message),
                                                        is_complete=True,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                        except Exception as e:
                            print '******************'
                            print e
                            print '******************'
                    else:
                        if dbphone[0]:
                            whatsapp = WhatsappReceived(phone=phone,
                                                        message='',
                                                        video=getMediaFromHttps(message),
                                                        is_valid=False,
                                                        is_complete=False,
                                                        date_creation=datetime.datetime.now())
                            whatsapp.save()
                else:
                    print '*******************************'
                    print 'Tipo de archivo desconocido'
                    print '*******************************'

        else:
            if type_message is 'image':
                image_whatsapp = getMediaFromHttps(message)
                whatsapp = WhatsappReceived(phone=phone,
                                            message='',
                                            image=image_whatsapp,
                                            is_valid=False,
                                            is_complete=False,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()
                try:
                    #ubal_value = anomaly_detector(image_whatsapp)
                    start_new_thread(anomaly_detector,(phone, image_whatsapp, whatsapp))
                except:
                    print "ERROR: PROBLEMA CON EL THREAD"

            elif type_message is 'audio':
                whatsapp = WhatsappReceived(phone=phone,
                                            message='',
                                            audio=getMediaFromHttps(message),
                                            is_valid=False,
                                            is_complete=False,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()
            elif type_message is 'video':
                whatsapp = WhatsappReceived(phone=phone,
                                            message='',
                                            video=getMediaFromHttps(message),
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
            print '++++++++++++++++++++++++++++++++++++='
            print 'en el else text'
            print '++++++++++++++++++++++++++++++++++++='
            whatsapp = WhatsappReceived(phone=phone,
                                        message=message,
                                        image=None,
                                        is_valid=True,
                                        is_complete=False,
                                        date_creation=datetime.datetime.now())
            whatsapp.save()
        else:
            print '=================================='
            print 'GUARDANDO UNA IMAGEN POR PRIMERA VEZ'
            print '=================================='
            image_whatsapp = getMediaFromHttps(message)
            whatsapp = WhatsappReceived(phone=phone,
                                        message='',
                                        image=image_whatsapp,
                                        is_valid=True,
                                        is_complete=False,
                                        date_creation=datetime.datetime.now())
            whatsapp.save()
            try:
                #ubal_value = anomaly_detector(image_whatsapp)
                start_new_thread(anomaly_detector,(phone, image_whatsapp, whatsapp))
            except:
                print "ERROR: PROBLEMA CON EL THREAD"


"""
def answer(risp, phone):
    print '**************************'
    print 'Phone: ' + phone
    print 'Message: ' + risp
    print '**************************'
    try:
        stack = YowsupSendStack(credential(), [([phone, risp])])
        stack.start()
    except:
        pass
    return
"""

while True:
    try:
        stack = YowsupReceiveStack(credential())
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
#        answer('Gracias por la imagen', phone)

    except MessageReceived as rcvd:
        received=rcvd.value
        phone = received[:11]
        message = received[11:]

        print '------------------------'
        print 'Phone: ' + phone
        print 'Message: ' + message
        print '------------------------'

        saveWhatsapp(phone=phone, type_message='text', message=message)
#        answer('Gracias por el mensaje', phone)

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


