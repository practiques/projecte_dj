# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<usuari_id>\d+)/$', views.usuari, name='usuari'),
    url(r'^(?P<carrec_id>\d+)/results/$', views.carrec, name='carrec'),
)