
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import urllib3, certifi

def getMediaFromHttps(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET',url)
    return r.data

def get_pagination(request, messages):
    paginator = Paginator(messages, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages = paginator.page(paginator.num_pages)

    return messages
