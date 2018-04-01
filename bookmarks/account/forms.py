# -*- coding:utf-8 -*- 
__author__ = 'John 2018/4/1 20:21'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
