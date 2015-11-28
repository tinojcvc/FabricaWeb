
from mongoengine import *
from cStringIO import StringIO
import cStringIO
from PIL import Image
import base64

connect('fabricaweb')

class WhatsappReceived(Document):
    phone = StringField(required=True)
    message = StringField(required=False)
    image = BinaryField(required=False, null=True)
    audio = BinaryField(required=False, null=True)
    video = BinaryField(required=False, null=True)
    is_valid = BooleanField(required=True, default=False)
    is_complete = BooleanField(required=True, default=False)
    is_read = BooleanField(required=True, default=False)
    location = StringField(required=False)
    date_creation = DateTimeField(required=True)


    def hola(self):
        data = StringIO(self.image)
        img = Image.open(data)
        resizeImg = img.resize((150,150), Image.ANTIALIAS)
        buffer = cStringIO.StringIO()
        resizeImg.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue())
        return img_str