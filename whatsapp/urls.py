
from django.conf.urls import patterns, url
from whatsapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='whatsapp'),
)
