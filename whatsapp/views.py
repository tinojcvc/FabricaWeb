
from django.shortcuts import render, redirect, render_to_response
from whatsapp.models import WhatsappReceived
from util.utils import get_pagination

from FabricaWeb.decorators import login_required

@login_required
def index(request):
    list_msg = WhatsappReceived.objects.filter(is_read=False).order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render(request, 'messages.html',
                  {'messages': messages, 'size': len(list_msg), 'home': True})

    #return render_to_response('whatsapp.html', {'phones': phones},
     #                         context_instance=RequestContext(request))

@login_required
def view_message(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_read=True)

    list_content = WhatsappReceived.objects.filter(id=message_id).order_by('-date_creation')
    #phone_number = WhatsappReceived.objects.get(id=message_id)

    return render(request, 'view_message.html', {'list_content': list_content})

@login_required
def no_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=False)
    return redirect('whatsapp')

@login_required
def is_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=True)
    return redirect('whatsapp')

@login_required
def view_all(request):
    list_msg = WhatsappReceived.objects.order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render(request,
                  'messages.html',
                  {"messages": messages, 'all_message': True})

@login_required
def view_read(request):
    list_msg = WhatsappReceived.objects.filter(is_read=True).filter(is_valid=True).order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render(request, 'messages.html',
                  {'messages': messages, 'view_read': True})

@login_required
def view_no_valid(request):
    list_msg = WhatsappReceived.objects.filter(is_valid=False).order_by('-date_creation')
    messages = get_pagination(request, list_msg)

    return render(request, 'messages.html',
                  {'messages': messages, 'view_no_valid': True})

