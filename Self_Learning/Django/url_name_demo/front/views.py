from django.shortcuts import render
from django.http import HttpResponse
# 重定向
from django.shortcuts import redirect,reverse


# Create your views here.

def index(request):
    # 如果没有传递usename=xxx,则返回前台首页
    # 如果没有直接跳转到登录页面
    # request.GET.get('username')在网页地址后接的字符串中获取用户名(字符)
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        # reverse的作用是将命名统一重定向到前面的相关联的路径,不管如何修改路径名都可以,节省了时间
        login_url = reverse('front:login')
        print('='*30)
        print(login_url)
        print('='*30)
        return redirect(login_url)
        # signin登录
        # signup注册

def login(rquest):
    return HttpResponse('前台登录页面')