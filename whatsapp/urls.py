
from django.conf.urls import url
from whatsapp import views

urlpatterns = [
    url(r'^$', views.index, name='whatsapp'),
    url(r'^view_message/(?P<message_id>\w+)/$', views.view_message, name='view_message'),
    url(r'^is_valid/(?P<message_id>\w+)/$', views.is_valid, name='is_valid'),
    url(r'^no_valid/(?P<message_id>\w+)/$', views.no_valid, name='no_valid'),
    url(r'^view_all/$', views.view_all, name='view_all'),
    url(r'^view_read/$', views.view_read, name='view_read'),
    url(r'^view_no_valid/$', views.view_no_valid, name='view_no_valid'),
]
