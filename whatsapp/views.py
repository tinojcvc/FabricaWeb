from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from whatsapp.models import WhatsappReceived

def index(request):
    list_msg = WhatsappReceived.objects.filter(is_read=False).order_by('-date_creation')
    return render(request, 'whats_online.html', {'list_msg':list_msg, 'size': len(list_msg)})

    #return render_to_response('whatsapp.html', {'phones': phones},
     #                         context_instance=RequestContext(request))

def view_message(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_read=True)

    list_content = WhatsappReceived.objects.filter(id=message_id).order_by('-date_creation')
    #phone_number = WhatsappReceived.objects.get(id=message_id)

    return render(request, 'view_message.html', {'list_content': list_content})

def no_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=False)
    return redirect('whatsapp')

def is_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=True)
    return redirect('whatsapp')

def view_all(request):
    list_msg = WhatsappReceived.objects.order_by('-date_creation')
    paginator = Paginator(list_msg, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages = paginator.page(paginator.num_pages)

    return render_to_response('whats_online_all.html', {"messages": messages})
#    return render(request, 'whats_online_all.html', {'list_msg':list_msg})

def view_read(request):
    list_msg = WhatsappReceived.objects.filter(is_read=True).filter(is_valid=True).order_by('-date_creation')
    return render(request, 'whats_online_read.html', {'list_msg':list_msg})

def view_no_valid(request):
    list_msg = WhatsappReceived.objects.filter(is_valid=False).order_by('-date_creation')
    return render(request, 'whats_online_invalid.html', {'list_msg':list_msg})

