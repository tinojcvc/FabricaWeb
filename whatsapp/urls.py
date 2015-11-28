
from django.conf.urls import patterns, url
from whatsapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='whatsapp'),
    url(r'^view_message/(?P<message_id>\w+)/', views.view_message, name='view_message'),
)
