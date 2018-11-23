from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('cms首页')
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse(f'{current_namespace}:login'))

def login(rquest):
    return HttpResponse('cms登录页面')