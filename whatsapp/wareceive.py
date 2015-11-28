from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import ImageDownloadableMediaMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import LocationMediaMessageProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import VCardMediaMessageProtocolEntity
from yowsup.stacks import YowStack
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_media              import YowMediaProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.axolotl                     import YowAxolotlLayer
from yowsup.common import YowConstants
from yowsup import env

class MessageReceived(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        print '------------------------'
        print 'El type del dato: ' + type(self.value)
        print '------------------------'
        return repr(self.value)

class MediaMessageReceived(Exception):
    def __init__(self, value, message_on_list):
        self.value = value
        self.message_on_list = message_on_list

    def __str__(self):
        return repr(self.value)

    def getListMessage(self):
        return self.message_on_list


class ReceiveLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if not messageProtocolEntity.isGroupMessage():
            if messageProtocolEntity.getType() == 'text':
                self.onTextMessage(messageProtocolEntity)
            elif messageProtocolEntity.getType() == 'media':
                self.onMediaMessage(messageProtocolEntity)
            else:
                print 'Tipo de dato desconocido: ' + messageProtocolEntity.getType()
    
    def onTextMessage(self,messageProtocolEntity):
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())
            
        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            messageProtocolEntity.getBody(),
            to = messageProtocolEntity.getFrom())

        self.toLower(receipt)
        raise MessageReceived(messageProtocolEntity.getFrom(False)+messageProtocolEntity.getBody())

    def onMediaMessage(self, messageProtocolEntity):
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())
        self.toLower(receipt)
        if messageProtocolEntity.getMediaType() in ("image", "audio", "video"):
            return self.getDownloadableMediaMessageBody(messageProtocolEntity)
        else:
            return "[Media Type: %s]" % messageProtocolEntity.getMediaType()

    def getDownloadableMediaMessageBody(self, message):
        """
        media_message = "[Media Type:{media_type}, Size:{media_size}, URL:{media_url}]".format(
        media_type = message.getMediaType(),
        media_size = message.getMediaSize(),
        media_url = message.getMediaUrl()
        )
        """
        media_message_dic = {'type': message.getMediaType(),
                             'size': message.getMediaSize(),
                             'url': message.getMediaUrl()}

        raise MediaMessageReceived(message.getFrom(False)+message.getMediaUrl(),
                                   message_on_list=media_message_dic)

class YowsupReceiveStack(object):

    def __init__(self, credentials):
        layers = (ReceiveLayer,
                  (YowAuthenticationProtocolLayer,
                   YowMessagesProtocolLayer,
                   YowReceiptProtocolLayer,
                   YowAckProtocolLayer,
                   YowMediaProtocolLayer),
                  YowAxolotlLayer,
                  YowCoderLayer,
                  YowCryptLayer,
                  YowStanzaRegulator,
                  YowNetworkLayer)

        self.stack = YowStack(layers)
        self.stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, credentials)
        self.stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
        self.stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
        self.stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())

    def start(self):
        print '-------------------------'
        print 'En el start de YowsupReceiveStack'
        print '-------------------------'
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop(count=4)
            #self.stack.loop(timeout = 0.5, discrete = 0.5)
        except AuthError as e:
            print("Authentication Error: %s" % e.message)
