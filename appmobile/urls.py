
from django.conf.urls import url
from appmobile import views

urlpatterns = [
    url(r'^$', views.index, name='appmobile'),
    url(r'^services/$', views.services, name='app_sevices'),
]


