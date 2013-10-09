# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<usuari_id>\d+)/$', views.usuari, name='usuari'),
)

#urlpatterns = patterns('',
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detall'),
#)