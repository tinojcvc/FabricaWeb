import urllib3,certifi
from cStringIO import StringIO
from PIL import Image
import base64


http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET','https://mmi268.whatsapp.net/d/H_b7E-6gFsYRxdBC-KQ9_FZWLQAABSVkcDMRHw/AilHXmGiFjvb-XBvhRDTXXxYdRg37F6KKhXbEFqjwCXX.jpg')
data = StringIO(r.data)
resized_image = Image.open(data)
decode = base64.b64encode(data.read())
print decode
#resized_image.show()