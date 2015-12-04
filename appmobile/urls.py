
from django.conf.urls import url
from appmobile import views

urlpatterns = [
    url(r'^services/$', views.services, name='app_sevices'),
]


