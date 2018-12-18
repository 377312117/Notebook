from django.http import HttpResponse

def showviews(request):
    return HttpResponse('我的第一个Django处理程序')

def sh_views(request):
    return HttpResponse('测试匹配逻辑')


# 通过正则表达式传参
def show1_views(request,year):
    return HttpResponse(f'传递进来的参数为:{year}')

def show2_views(request,year,month,day):
    return HttpResponse(f'生日为:{year}年{month}月{day}日')


# 通过kwargs传参
def show3_views(request,name,age):
    return HttpResponse(f'姓名:{name},年龄:{age}')

def show4_views(request,year,month,day):
    return HttpResponse(f'<h1>生日为:{year}年{month}月{day}日</h1>')

