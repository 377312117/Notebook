from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def login_views(request):
    return HttpResponse('这是index下的login视图')

def register_views(request):
    return HttpResponse('这是index下的register视图')

def index_views(request):
    return HttpResponse('这是index下的index视图')

def temp_views(request):
    # 通过loader加载模板
    t=loader.get_template('01-temp.html')
    # 将模板渲染成字符串
    html=t.render()
    # 将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)

def temp02_views(request):
    return render(request,'02-temp.html')


def sayHi():
    return 'Hello,this is a function ...'

class Animals(object):
    name = '王富贵'
    def eat(self):
        return '王富贵吃了一条香肠'

def var_views(request):
    str1 = '这是模板中的字符串'
    num1 = 3306
    tup1 = ('西游记','水浒传','三国演义','红楼梦')
    lst1 = ['孙悟空','西门庆','曹操','林黛玉']
    dic1 = {
        'BJ':'北京',
        'SZ':'深圳',
        'SH':'上海',
    }
    dog = Animals()
    ret = sayHi()
    return render(request,'03-var.html',locals())


# 演示静态文件的处理
def static_views(request):
    # dic = {'static':'/static/images/500.jpg'}
    return render(request,'04-static.html')