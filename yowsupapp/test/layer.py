from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers                                     import YowLayer

class EchoLayer(YowLayer):

    def receive(self, protocolEntity):
        if protocolEntity.getTag() == "message":
            self.onMessage(protocolEntity)

    def onMessage(self, messageProtocolEntity):

        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            messageProtocolEntity.getBody(),
            to = messageProtocolEntity.getFrom()
        )

        self.toLower(outgoingMessageProtocolEntity)
