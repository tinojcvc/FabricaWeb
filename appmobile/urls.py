
from django.conf.urls import patterns, url
from appmobile import views

urlpatterns = patterns('',
    url(r'^services/$', views.services, name='app_sevices'),
)


