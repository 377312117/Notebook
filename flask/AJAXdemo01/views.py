'''
此模块用于配置路由映射函数以及反馈给客户端的视图
'''

import os
from datetime import datetime
import json

from flask import Flask, redirect, render_template, request,make_response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_

from config import *
from models import *



  


@app.errorhandler(404)
def page_not_found(e):
    '''用于无法找到页面时的404提示'''
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    '''用于服务器出现错误时的提示'''
    return render_template('500.html'), 500

@app.route('/01-xhr',methods=['GET','POST'])
def index():
    '''用于查看XMLHttpRequest'''
    if request.method == 'GET':
        return render_template('/01-xhr.html')


@app.route('/server',methods=['GET','POST'])
def server():
    '''用于测试ajax的使用'''
    uname=request.args.get('uname','')
    print('用户名:',uname)
    return '我的第一个AJAX请求'


@app.route('/02-homework',methods=['GET','POST'])
def homework():
    '''家庭作业'''
    return render_template('/02-homework.html')

@app.route('/03-server',methods=['GET','POST'])
def serverinfo():
    '''用于测试ajax的使用'''
    uname=request.args.get('lname','')
    user = Users.query.filter_by(name=uname).first()
    print('用户名:',uname)
    if user:
        return '用户名已经存在'
    else:
        return '用户名不存在'

@app.route('/04-post',methods=['GET','POST'])
def postmethod():
    '''用于测试xhr的post方式提交数据'''
    return  render_template('/04-post.html')

@app.route('/05-server',methods=['GET','POST'])
def postinfo():
    '''用于测试ajax的使用'''
    uname=request.form.get('uname','')
    uage=request.form.get('uage','')
    print('用户名:',uname)
    return f'uname:{uname},uage:{uage}岁' 


@app.route('/06-form',methods=['GET','POST'])
def form():
    '''用于测试xhr的post方式提交数据'''
    if request.method == 'GET':
    	return  render_template('/06-form.html')
    else:
        uname=request.form.get('uname','')
        uage=request.form.get('uage','')
        print('用户名:',uname)
        return f'uname:{uname},uage:{uage}岁'  

@app.route('/07-json',methods=['GET','POST'])
def jsonpost():
    '''用于测试xhr的post方式提交数据'''
    if request.method == 'GET':
    	return  render_template('/07-json.html')
    else:
        uname=request.form.get('uname','')
        uage=request.form.get('uage','')
        print('用户名:',uname)
        return f'uname:{uname},uage:{uage}岁' 

@app.route('/08-json',methods=['GET','POST'])
def jsonserver():
    '''用于测试json对象的后台处理'''
    return render_template('/08-json.html')

@app.route('/09-server',methods=['GET','POST'])
def jsontest():
    '''用于测试json对象的后台处理'''
    lst = ['王老六','RapWang','隔壁老王']
    dic = {
        'name':'王老六',
        'age':36,
        'gender':'男'
    }
    # 将list转换为json格式字符串
    jsonStr=json.dumps(dic)
    return jsonStr

@app.route('/10-server',methods=['GET','POST'])
def server10():
    '''用于测试json对象的后台处理模型实例'''
    user = Users.query.filter_by(id=1).first()
    jsonStr = json.dumps(user.to_dic())
    return jsonStr

@app.route('/11-json',methods=['GET','POST'])
def json_user():
    '''用于测试json对象的后台处理'''
    return render_template('/11-json.html')