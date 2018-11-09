from django.shortcuts import render # render渲染模板
from django.http import  HttpResponse
# 一些预置的数据类型
from django.urls import converters

# Create your views here.

def book(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id,category_id):
    # 可以从数据库中根据book_id提取这个图书的信息
    text = '您获取的图书id是 %s,图书分类是%s' % (book_id,category_id)
    return HttpResponse(text)

def author_detail(request):
    # 使用get请求进行映射,不需要将响应内容写在urls.py中
    author_id = request.GET['id']
    text = '作者id是 %s' % author_id
    return HttpResponse(text)

def publisher_detail(request,publisher_id):
    text = '出版社的id是:%s' % publisher_id
    return HttpResponse(text)