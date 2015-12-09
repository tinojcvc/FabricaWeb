from django.conf.urls import url
from appmobile import views

urlpatterns = [
    url(r'^$', views.index, name='appmobile'),
    url(r'^services/$', views.services, name='app_sevices'),
    url(r'^view_message/(?P<message_id>\w+)/$', views.view_message, name='view_message'),

]


