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
# 新导入include函数,以便不同应用下的urls进行匹配
from django.urls import path,include
# 根据面向对象的思想,分别在每个应用创建自己的视图,不同应用的的视图导入该主应用的urls.py中即可
from book import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # 所有匹配book开头的url都会转到book应用下的urls进行匹配
    path('book/',include('book.urls'))
]
