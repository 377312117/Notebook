from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from  django.core.exceptions import ObjectDoesNotExist
import logging
from django.contrib.auth.hashers import make_password
from django.db import DatabaseError
# Create your views here.

auth_check = 'MarceArhut'

def register_in(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        user = UserInfo()
        user.uname = request.POST.get('uname','')
        try:
            usertest = UserInfo.objects.filter(uname=user.uname)
            if usertest:
                return render(request,'register.html',{'message':'该用户已存在'})
        except ObjectDoesNotExist as e:
            loggin.warning(e)
        if request.POST.get('upassword') != request.POST.get('reupassword'):
            return render(request,'register.html',{'message':'两次密码不一致'})
            # make_password() 
            # 参数1:需要加密的密码
            # 参数2:任意的字符串
            # 参数3.加密的方式
        sha1_pwd=make_password(request.POST.get('upassword'),auth_check,'pbkdf2_sha1')
        user.upassword = sha1_pwd
        user.email = request.POST.get('uemail','')
        try:
            user.save()
        except DatabaseError as e:
            logging.warning(e)
        return render(request, 'register.html', {"message":"注册成功"})
