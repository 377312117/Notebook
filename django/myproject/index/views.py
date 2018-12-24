from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import RemarkForm,RegisterForm

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
    return render(request,'04-static.html')
def alias01_views(request):
    # 在视图中解析
    url = reverse('a02',args=(2015,))
    print('a02的地址为:'+url)
    return render(request,'05-alias01.html')

def alias02_views(request,year):
    print('年份为:'+year)
    return render(request,'06-alias02.html')


def addbook_views(request):
    '''此例子演示如何数据库的增加数据的操作'''
    # # 方式1:Entry.objects.create()
    Book.objects.create(title='WEB基础',publicate_date='2016-10-12')
    Book.objects.create(title='人工智能',publicate_date='2017-10-12')
    Book.objects.create(title='数据库进阶',publicate_date='2018-10-12')
    Book.objects.create(title='网络编程',publicate_date='2019-10-12')
    # # 新增加书籍的返回值
    # print(f'新增加的书籍的ID为:{book.id}')
    # 方法2
    # book = Book(title='数据库基础')
    # book.publicate_date = '2016-12-12'
    # book.save()
    # 方法3
    # dic = {
    #     '属性':'值',
    #     '属性':'值',

    # }
    # obj.Entry(**dic)
    # obj.save()
    return HttpResponse('Add Book Success')


def querybook_views(request):
    '''此例子演示如何数据库的查询数据的操作'''
    # 基本的查询操作
    # 1.all()
    # books = Book.objects.all()
    # print(f'查询book的结果为:{books}')
    # for book in books:
    #     print(f'ID:{book.id},书名:{book.title},出版日期:{book.publicate_date}')
    # # 2.value()
    # books = Book.objects.all().values('title')
    # print(f'查询book的结果为:{books}')
    # # 查询book的结果为:<QuerySet [{'title': 'Python编程基础'}, {'title': '数据库基础'}]>
    # for book in books:
    #     print(f'查询结果为{book["title"]}')
    # # 3.value_list()
    # books = Book.objects.all().values_list('title')
    # print(f'values_list()查询book的结果为:{books}')
    # # 查询book的结果为:<QuerySet [{'title': 'Python编程基础'}, {'title': '数据库基础'}]>
    # for book in books:
    #     print(f'查询结果为{book}')
    # # 4.get
    # books = Book.objects.get(id=1)
    # print(f'get()查询book的结果为:{books.title}')
    # 方法5
    lst = Book.objects.filter(id=1)
    for l in lst:
        print(f'l为{l.title}')
    return HttpResponse('query Book Success')

# @csrf_protect
def postinfo_views(request):
    if request.method == 'GET':
        return render(request,'09-postinfo.html')
    else:
        uname = request.POST.get('uname','')
        upassword = request.POST.get('upassword','')
        print(f'uname:{uname},upassword:{upassword}')
        return HttpResponse(f'uname:{uname},upassword:{upassword}')


def remarkform_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'10-remarkform.html',locals())
    else:
        # 通过RemarkForm的构造函数,接收请求提交数据
        form = RemarkForm(request.POST)
        # 通过验证
        if form.is_valid():
            # 通过验证后取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse('取值成功')


def modelform_views(request):
    if request.method == 'GET':
        # 创建RegisterForm对象,并发送到模板上
        form = RegisterForm()
        return render(request,'11-modelform.html',locals())
    else:
        # 通过RemarkForm的构造函数,接收请求提交数据
        form = RegisterForm(request.POST)
        # 通过验证
        if form.is_valid():
            # 通过验证后取值
            user = Uses(**form.changed_data)
            print(user)
        return HttpResponse('取值成功')
        