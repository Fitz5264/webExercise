from django.contrib import admin
from django.conf.urls import url
from system.views import *
urlpatterns=[
    url(r'^login/$',login,name='login'),
    url(r'^login/Action/$',loginAction,name='loginAction'),
]