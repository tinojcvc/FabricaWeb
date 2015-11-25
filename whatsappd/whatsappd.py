from wasend import YowsupSendStack
from wareceive import YowsupReceiveStack, MessageReceived

def credential():
     return "59100000000", "kgWT7zbZhFxGEl/fJoVGwn/Kzbw"

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

