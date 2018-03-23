# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/23 15:41'

from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
