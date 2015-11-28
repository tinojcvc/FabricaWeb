
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
        try:
            data = StringIO(self.image)
            img = Image.open(data)
            resizeImg = img.resize((150,150), Image.ANTIALIAS)
            buf = cStringIO.StringIO()
            resizeImg.save(buf, format="JPEG")
            img_str = base64.b64encode(buf.getvalue())
            return img_str
        except Exception:
            return "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAQAAABpN6lAAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2tpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDozODlCNTNERTdDMjE2ODExODIyQUMxQTMzQkUzQUE5QiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDozRDc0ODY3ODcwN0MxMUUzOEU5QzlDNDIzMURBMUE1MSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDozRDc0ODY3NzcwN0MxMUUzOEU5QzlDNDIzMURBMUE1MSIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpjOGU4NzNmZi0zOWY1LTQ2OTctYTkxNS1mNmM1YWRmZDllM2EiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6Mzg5QjUzREU3QzIxNjgxMTgyMkFDMUEzM0JFM0FBOUIiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4tcrurAAAEpElEQVR42u3dbVfaSBiAYf///xnE2GpUqBLXui7FAl3TuuzZsmeJnrRKa9Te+yEPIUEYoAVOCA/zRZIJk7km88LMcNziE7cbHD5u8cQmvx63uN1ogBsFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFUAAFWMbrC7/hYKyhzDH/FROgR3lK5ofhungAz7yeOfuGbfrrCPDEZxqcURsTqnNk32A4oMYZDT4vayvTogGeuZpav38uOFzxnHeA73OX8Hyhyvc8AzxxuNTsGwyHi64KiwSoLz37BkM9rwB3lJKbfE1l5gy94oxLWlxyOrH12OF33srZEvf5BGgmt1vhGfgwQ+Y9evxIfcYPumNakT2+SQsTd6HNfAIMy/w9AOGUzO/SnfBJ12xPGA79JcC5BNhJbrgpA15b9vetD/JN6tMM/6ZGkXGFyCWAmQNgJ5X9O9p4VKjR5EuKYNiiNJKjDTmy9gB/J3X+MpVRQ4k/km6unTr6J4884Cdx1xygkowaa2POvhEC27eGNQcYlP/7Cecv5PyHYgKUeATg20hbnw5fAfhaTIAjie9b2oi2xHGKCHAm8c8tADWJc1REgHOJX7MADJ6SN0UEOJX4b2d4Ag6KCOBK/CsLQFNGCeVidoPxpMZ9ZgiUDfGI8Lao4wBfrng3pZVoFBVgT+b2nsY2codEADxYps/X/rtAO5lEO3/RRD7IuQvL9WsPUKKXXHfLOyrsc0SdIDnasX6ZziXA9lzzAWXrwte1pYE0bOcTwJ0LwFCiPXae/3Hq5KqbT4CLkcHuPzPMCe7hy3wf0jW22Z161UU+AXqZjqyZmdSaxnDCKce8mjF+L6/rAscrWRc4zu/CyP0cpf6zYYe7/ALAzQw1+FfCLjeQZwC452Rp2T9Z7JrQcgDi5rDOvrUnny+UOaC+2KZvuQBr9VIABVAABVAABVAABVAABVAABVAABVAABZj91ZWlkHMCoIVHSIjHuSxugoeXih/HiI8OlsCCTJwAL7UpMqIle4Q8ukCIlwota1orAAjl1lxZqfEwBASZnZ3ZVbw4BrK2E9+4m4njYSQORFQxOJKCQ18+e7jN2pbWCgB8DC35KxwBGOwAmAwQX+tnljr7mY2xPgaXUJ6dDhBgMqVsS2sFAB0MDp3kV11DACcpRxuASa3/xq8GRh76PlDF0MmkOA5gUlorAIiSff3eyBPg0ZCHdjKAn5TeIE6EwRAJA/Iubjk8PDojVQBrWivqBbo0cDA4IwBx+VUtAIMYw5KLH3lfMhRz9AXAxeBLiQ8aQaxprQQglJJzMQQjAFGyWD4JIMQQpgDcTPl28FJ7ifwEwBtTJcaltQKAFoYGAV0cDNEIAIRSPycBkGm9OxhcAgICeRa60lQG0t3GAC6+hI41rZU0gk7mBw2jAINNLrMBeJkmL36m/MzvBcOx3eCktFZSBSI6+PjSb4cEREQEUjUGx8i8i4AgczR+F7yI2Qf6UtqDkUGQCqE1LR0KK4ACKIACKIACKIACKIACKIACKIACKIACKIACKIACKIACKIACKIACKIACvADY+H++/pGbDQ7+/y8MV3904l8kAAAAAElFTkSuQmCC"
