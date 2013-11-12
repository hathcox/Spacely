# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from spacely.forms.signupform import SignupForm
from spacely.models.user import UserManager
from spacely.config.strings import *


def home(request):
    return render(request, 'index.html', None)


def about(request):
    return render(request, 'about.html', None)


def contact(request):
    return render(request, 'contact.html', None)


def signup(request):
    userManager = UserManager()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            userManager.create_user(username, password, email)

            messages.success(request, ACCOUNT_CREATED_SUCCESFULLY_MESSAGE)
            request.path = "/dummy"
            return HttpResponseRedirect(request.path)
    else:
        form = SignupForm()  # An unbound form

    return render(request, 'signup.html', {'form': form})


def dummy(request):
    return render(request, 'dummy.html', None)
