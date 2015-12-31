
from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.home, name='accounts'),
    url(r'^sigin/$', views.sigin, name='sigin'),
    url(r'^register/$', views.register, name='register'),
]
