# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from celery import task
from spacely.forms.login import LoginForm
import logging, sys

# Get an instance of a logger
logger = logging.getLogger(__name__)


def playview(request):
    ''' Load the static page '''
    return render(request, 'play.html')


