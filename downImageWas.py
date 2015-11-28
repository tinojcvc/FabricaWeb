import urllib3,certifi
from cStringIO import StringIO
import cStringIO
from PIL import Image
import base64

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET','https://mmi268.whatsapp.net/d/H_b7E-6gFsYRxdBC-KQ9_FZWLQAABSVkcDMRHw/AilHXmGiFjvb-XBvhRDTXXxYdRg37F6KKhXbEFqjwCXX.jpg')
data = StringIO(r.data)

img = Image.open(data)
resizeImg = img.resize((250,250), Image.ANTIALIAS)
buffer = cStringIO.StringIO()
resizeImg.save(buffer, format="JPEG")
img_str = base64.b64encode(buffer.getvalue())
print img_str
#resized_image.show()