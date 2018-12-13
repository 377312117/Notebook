"""
此中包含了所有需要创建的模型类
使用数据库进行管理
"""

import sys
sys.path.append(r'/Users/zhaozhengxing/Documents/OneDrive/python3/flask/BlogNew/app/')
from config import app,db


class Users(db.Model):
    '''
        用户信息表
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean, default=True)

    def __init__(self, name, email,password,phonenumber):
        # 用于实例对象进行赋值
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.password=  password

    def __repr__(self):
        return f'<User:{self.name}>'
    
    def to_dic(self):
        dic = {
            'id':self.id,
            'name':self.name,
            'password':self.password,
            'phonenumber':self.phonenumber,
            'email':self.email,
            'isActive':self.isActive,
        }
        return dic
  
class Citys(db.Model):
    '''
        城市表
    '''
    __tablename__ = 'citys'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(80), unique=True, nullable=False)
    p_id = db.Column(db.Integer, db.ForeignKey('provinces.id'))

    def __init__(self, cname):
        # 用于实例对象进行赋值
        self.cname = cname

    def __repr__(self):
        return f'<User:{self.cname}>'
    
    def to_dic(self):
        dic = {
            'id':self.id,
            'cname':self.cname,
        }
        return dic

class Provinces(db.Model):
    '''
        省份表
    '''
    __tablename__ = 'provinces'
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    citys = db.relationship('Citys', backref='province', lazy='dynamic')

    def __init__(self, pname):
        # 用于实例对象进行赋值
        self.pname = pname

    def __repr__(self):
        return f'<User:{self.pname}>'
    
    def to_dic(self):
        dic = {
            'id':self.id,
            'pname':self.pname,
        }
        return dic
   
    