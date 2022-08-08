# -*- coding: utf-8 -*-

"""
@author: jiruichang
@software: PyCharm
@file: urls.py
@time: 2022/8/7 19:33
"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认身份的身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 注册界面
    path('register/', views.register, name='register'),
]