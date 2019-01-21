"""Fruitday URL Configuration

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

urlpatterns = [
    url('admin/', admin.site.urls),
    # 访问路径是以userinfo/开始的时候,将请求交给userinfo中的urls.py去处理
    url(r'^userinfo/',include('userinfo.urls')),
    url(r'^memberapp/',include('memberapp.urls')),
    url(r'^cartinfo/',include('cartinfo.urls')),
    # 只要没有特定的访问路径,则交给index应用去处理
    url(r'^',include('index.urls')) ,

]