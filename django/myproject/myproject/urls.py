"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
# 在视图中导入视图函数
from .views import *

dic= {
    'name':'wangwc',
    'age':18
}
dic1= {
    'year':2018,
    'month':12,
    'day':24
}


urlpatterns = [
    
    # 当访问路径为/show,对匹配路由不进行^$约束时,只要含有路由关键字都可匹配,
    # 匹配顺序从上往下,优先匹配顺序在前的路由视图,尤其注意不完全匹配,部分的内容匹配到就会进行匹配,sh也会匹配show
    # url(r'sh',sh_views),
    # url(r'^show/$',showviews),
    url(r'^show/(\d{4})/$',show1_views),
    url(r'^show2/(\d{4})/(\d{1,2})/(\d{1,2})/$',show2_views),
    url(r'^show3/$',show3_views,dic),
    url(r'^show4/$',show4_views,dic1),
    # 访问路径是以music/开始的时候,将请求交给music中的urls.py去处理
    url(r'^music/',include('music.urls')),
    url(r'^news/',include('news.urls')),
    url(r'^sport/',include('sport.urls')),
    # 只要没有特定的访问路径,则交给index应用去处理
    url(r'^',include('index.urls')) 
]
