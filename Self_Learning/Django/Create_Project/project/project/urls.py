"""project URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from book import views

def index(request):
    return  HttpResponse('豆瓣首页')





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('MyApp.urls')),

    # 127.0.0.1:8000/book/
    path('book/',views.book) , # 前面是路径,后面是响应函数(内容)
    path('book/detail/<book_id>/<category_id>',views.book_detail),
    path('book/author/',views.author_detail),
    # 注意author后面的斜杆一定要有
    path('book/publisher/<uuid:publisher_id>/',views.publisher_detail)
    # uuid,int是django规定的字符串类型,选择哪种就只能用哪种来访问该页面
    # uuid是无规律的32位的字码,可由import uuid 中的uuid4()生成
]
