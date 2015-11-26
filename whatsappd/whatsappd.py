from wasend import YowsupSendStack
from wareceive import YowsupReceiveStack, MessageReceived

from mongoengine import *

import datetime

connect('fabricaweb')

class WhatsappReceived(Document):
    phone = StringField()
    message = StringField()
    date = DateTimeField()

def credential():
     return "59167479531", "kgWT7zbZhFxGEl/fJoVGwn/Kzbw="

while True:
    try:
        stack=YowsupReceiveStack(credential())
        stack.start()
    except MessageReceived as rcvd:
        received=rcvd.value
        phone = received[:11]
        message = received[11:]

        print '------------------------'
        print 'Phone: ' + phone
        print 'Message: ' + message
        print '------------------------'

        dbphone = WhatsappReceived.objects.filter(phone=phone).order_by('-date')
        len_dbphone = len(dbphone)
        if len_dbphone > 0:
            print '------------------'
            print 'El telefono existe'
            print '------------------'
            now = datetime.datetime.now()
            if dbphone[0].date.date() == now.date():
                time = dbphone[0].date + datetime.timedelta(minutes=30)
                if now < time:
                    last_message = dbphone[0].message
                    print '-----------------'
                    print dbphone[0].date.date()
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
                    print '------------------'
                    print 'nuevo mensaje del numero: ' + phone
                    print '------------------'
                    whatsapp = WhatsappReceived(phone=phone,
                                                message=message,
                                                date=datetime.datetime.now())
                    whatsapp.save()
            else:
                whatsapp = WhatsappReceived(phone=phone,
                                            message=message,
                                            date=datetime.datetime.now())
                whatsapp.save()
        else:
            whatsapp = WhatsappReceived(phone=phone,
                                        message=message,
                                        date=datetime.datetime.now())
            whatsapp.save()

