from layer4 import EchoLayer
from yowsup.layers.auth                        import (YowAuthenticationProtocolLayer,
                                                      AuthError)
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YOWSUP_CORE_LAYERS
from yowsup import env
from demo2.wareceive import MessageReceived

#import logging
#logging.basicConfig(level=logging.DEBUG)

CREDENTIALS = ("59167479531", "kgWT7zbZhFxGEl/fJoVGwn/Kzbw=") # replace with your phone and password

if __name__==  "__main__":
    layers = (
        EchoLayer,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer)
    ) + YOWSUP_CORE_LAYERS

    print '---------------------------'
    print YowAuthenticationProtocolLayer.PROP_CREDENTIALS
    print YowNetworkLayer.PROP_ENDPOINT
    print YowConstants.ENDPOINTS[0]
    print YowCoderLayer.PROP_DOMAIN
    print YowConstants.DOMAIN
    print YowCoderLayer.PROP_RESOURCE
    print env.CURRENT_ENV.getResource()
    print '---------------------------'
    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())          #info about us as WhatsApp client

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    try:
        stack.loop() #this is the program mainloop
        #stack.start()
        #except AuthError as error:
    except MessageReceived as rcvd:
        print '------------------------'
        print rcvd.value.lower()
        print '------------------------'

