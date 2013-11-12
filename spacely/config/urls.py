# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^$', 'spacely.views.index.home'),
    url(r'^about$', 'spacely.views.index.about'),
    url(r'^contact$', 'spacely.views.index.contact'),
    url(r'^signup$', 'spacely.views.index.signup'),
    url(r'^dummy$', 'spacely.views.index.dummy'),
    url(r'^logout$', 'spacely.views.login.logoutview'),
    url(r'^login$', 'spacely.views.login.loginview'),
    url(r'^play$', 'spacely.views.play.playview'),

)
