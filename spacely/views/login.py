# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login

from spacely.forms.login import LoginForm


def loginview(request):
    login_error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,
                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/member")
                else:
                    login_error = True
            else:
                login_error = True
    else:
        form = LoginForm()  # An unbound form

    return render(request, 'login.html',
        {'form': form, 'login_error': login_error})


def logoutview(request):
    logout(request)
    return render(request, 'index.html', None)
