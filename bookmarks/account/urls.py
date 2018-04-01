# -*- coding:utf-8 -*- 
__author__ = 'John 2018/4/1 23:16'

from django.urls import path

from .views import user_login


urlpatterns = [
    path('login/', user_login, name='login'),
]