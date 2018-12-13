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

@app.route('/01-test')
def test1():
        return render_template('/01-test.html')

@app.route('/02-jsoninfo')
def jsoninfo():
    # user = Users.query.filter_by(id=1).first()
    users = Users.query.all()
    allusers=[]
    for u in users:
        allusers.append(u.to_dic())
    jsonStr = json.dumps(allusers)
    print(f'jsonStr:{jsonStr}')
    return jsonStr





@app.route('/03-jsonpro')
def jsonpro():
    return render_template("/03-jsonpro.html")


@app.route('/04-provinceinfo')
def provinceinfo():
    provinces= Provinces.query.all()
    allprovinces=[]
    for p in provinces:
        allprovinces.append(p.to_dic())
    jsonStr = json.dumps(allprovinces)
    print(f'jsonStr:{jsonStr}')
    return jsonStr

@app.route('/05-loadcity')
def loadcity():
    p_id = request.args.get('p_id')
    cities = Citys.query.filter_by(p_id=p_id).all()
    lst = []
    for c in cities:
        lst.append(c.to_dic())
    jsonStr = json.dumps(lst)
    return jsonStr

@app.route('/06-jq-load',methods=['GET','POST'])
def jqLoad():
    uname=request.form.get('uname')
    uage=request.form.get('uage')
    return f'使用{request.method}方式传递进来的数据为uname={uname},uage={uage}'

@app.route('/07-jq-get')
def jq_get():
    dic = {
        'uname':'wangwc',
        'uage':30
    }
    return json.dumps(dic)


@app.route('/08-jq-post',methods=['POST','GET'])
def jq_post():
    uname = request.form.get('uname','')
    ugender = request.form.get('ugender','')
    print(f'uname:{uname},ugender:{ugender}')
    return f'uname:{uname},ugender:{ugender}'


@app.route('/09-jq-register',methods=['POST','GET'])
def jq_register():
    uname = request.args.get('uname','')
    print('uname:',uname)
    user = Users.query.filter_by(name=uname).first()
    print('user:',user)
    if user:
        dic ={
            'status':1,
            'text':'用户名称已经存在'
        }
    else:
        dic ={
            'status':0,
            'text':'用户名可用'
        }
    return json.dumps(dic)

@app.route('/10-jq-ajax',methods=['POST','GET'])
def jq_ajax():
    users = Users.query.all()
    print('users:',users)
    lst=[]
    for u in users:
        lst.append(u.to_dic())
    return json.dumps(lst)


@app.route('/11-jq-insertinfo',methods=['POST','GET'])
def jq_insertinfo():
    uname = request.form.get('uname','')
    upassword = request.form.get('upassword','')
    phonenumber = request.form.get('phonenumber','')
    user = Users.query.filter_by(name=uname).first()
    try:
        user = Users(name=uname,password=upassword,phonenumber=phonenumber,email=None)
        db.session.add(user)
        db.session.commit()
        dic ={
            'status':1,
            'text':'恭喜你,注册成功'
        } 
        return json.dumps(dic)
    except Exception as e:
        dic ={
            'status':0,
            'text':'用户名称已经存在'
        } 
        return json.dumps(dic)

@app.route('/11-server',methods=['POST','GET'])
def servertest():
    
    callback = request.args.get('callback','')
    print(f'callback:{callback}')
    return f'{callback}("这是服务端的响应内容");'

@app.route('/12-server',methods=['POST','GET'])
def servertest2():
    callback = request.args.get('callback','')
    dic={
        'flightNO':'ca977',
        'from':'BeiJing',
        'to':'LA',
        'time':'00:30'
    }
    data = json.dumps(dic)
    print('data:',callback+"("+data+");")
    return callback+"("+data+");"



@app.route('/13-server',methods=['POST','GET'])
def jq_cross():
    callback = request.args.get('callback','')
    return f'{callback}("服务器响应回去的数据")'
