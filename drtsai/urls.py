
from django.conf.urls import url, include
from django.urls import path
from drtsai import views

urlpatterns = [
    # path("",views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^welcome$', views.index),
    path("his/<name>", views.his, name="his" ),
    url(r'^index$', views.index),    
    # url(r'^his$', views.his, name="his"),      
    # url(r'^his/?(?P<name>[\w]*)', views.his, name="his"),       
]