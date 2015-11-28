from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from datetime import datetime
from whatsapp.models import WhatsApp

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


# Create your views here.
def index(request):
    phone_number =
    return render_to_response('index.html', {'stations': stations},
                              context_instance=RequestContext(request))