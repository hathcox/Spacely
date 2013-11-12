# -*- coding: utf-8 -*-
from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    repeated_password = forms.CharField(max_length=32,
        widget=forms.PasswordInput)
    email = forms.EmailField()
    terms = forms.BooleanField(required=True)
