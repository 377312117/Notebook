'''
此模块用于配置路由映射函数以及反馈给客户端的视图
'''

import os
from datetime import datetime
import json

from flask import Flask, redirect, render_template, request,make_response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_

from . import main
from .. import db
from ..models import *


@main.errorhandler(404)
def page_not_found(e):
    '''用于无法找到页面时的404提示'''
    return render_template('/404.html'), 404


@main.errorhandler(500)
def internal_server_error(e):
    '''用于服务器出现错误时的提示'''
    return render_template('/500.html'), 500

@main.route('/01-test')
def test1():
        return '这是main下的视图'

@main.route('/')
def main_index():
    categories = Category.query.all()
    print('categories:',categories)
    # 读取前5条信息
    topics = Topic.query.limit(5).all()
    if 'uid' in session and 'loginname' in session:
        user = User.query.filter_by(ID=session.get('uid')).first()
    return render_template('index.html',params=locals())

