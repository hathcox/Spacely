# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'offRoad.views.home', name='home'),
    url(r'^', include('spacely.config.urls')),

    # urls for openid
    url(r'', include('social_auth.urls')),

    # urls for socketio
    url(r'', include('django_socketio.urls')),

    # urls for the admin
    #url(r'^admin/', include(admin.site.urls)),
)
