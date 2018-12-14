"""
Users中的视图以及路由函数
"""


import os
from datetime import datetime
import json

from flask import Flask, redirect, render_template, request,make_response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_

from . import users
from ..models import *

@users.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("/login.html")
    else:
        loginname = request.form.get('username')
        upwd = request.form.get('password')
        url = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            session['uid']=user.ID 
            session['loginname']=loginname
            resp = redirect(url)
            resp.delete_cookie('url')
            return resp
        else:
            return render_template(url,errMsg='用户或者密码不正确')

@users.route('/logout')
def logout():
    if 'uid' in session and 'loginname' in session:
        del session['uid']
        del session['loginname']
    url = request.headers.get('Referer','/')
    return redirect(url)

