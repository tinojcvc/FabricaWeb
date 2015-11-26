
from wasend import YowsupSendStack
from wareceive import YowsupReceiveStack, MessageReceived

from mongoengine import *

import datetime

connect('fabricaweb')

class WhatsappReceived(Document):
    phone = StringField(required=True)
    message = StringField(required=False)
    image = StringField(required=True)
    audio = BinaryField(required=False)
    video = BinaryField(required=False)
    is_valid = BooleanField(required=True)
    location = StringField(required=False)
    date_creation = DateTimeField(required=True)

def credential():
     return "59100000000", "password"

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

