"""
此中包含了所有需要创建的模型类
使用数据库进行管理
"""

# 导入db以便在实体类中使用
from . import db

class User(db.Model):
    '''
        用户信息表
    '''
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    upwd = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), unique=True)
    url = db.Column(db.String(200))
    is_author = db.Column(db.Boolean,default=False)
    # 定义与Topic的关联关系和反向引用
    topics = db.relationship('Topic',backref='user',lazy='dynamic')
    # 定义与Reply的关联关系和反向引用
    replies = db.relationship('Reply',backref='user',lazy='dynamic')
    # 增加多(User)对多(Topic)的反向的关联属性和反向引用关系
    voke_topics = db.relationship('Topic',
        secondary='voke',lazy='dynamic',
        backref=db.backref(
            'voke_users',
            lazy='dynamic'
        )
    )

    def __init__(self, loginname,uname,upwd, email,url,is_author):
        # 用于实例对象进行赋值
        self.loginname = loginname
        self.uname = uname
        self.upwd = upwd
        self.email = email
        self.url = url
        self.is_author= is_author

    def __repr__(self):
        return f'<User:{self.loginname}>'
    
    def to_dic(self):
        dic = {
            'loginname':self.loginname,
            'uname':self.uname,
            'upwd':self.password,
            'url':self.url,
            'email':self.email,
            'is_author':self.is_author,
        }
        return dic

class Topic(db.Model):
    '''
        文章信息表
    '''
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text)
    # 关系:一(Category)对多(Topic)的关系
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    # 关系:一(Blogtpye)对多(Topic)的关系
    blogtype_id = db.Column(db.Integer,db.ForeignKey('blogtype.id'))
    # 关系:一(User)对多(Topic)的关系
    user_id = db.Column(db.Integer,db.ForeignKey('user.ID'))
    # 定义与Reply的关联关系和反向引用
    replies = db.relationship('Reply',backref='topic',lazy='dynamic')

    def __init__(self, title,pub_date,read_num, content,images):
        # 用于实例对象进行赋值
        self.title = title
        self.pub_date = pub_date
        self.read_num = read_num
        self.content = content
        self.images = images

    def __repr__(self):
        return f'<User:{self.title}>'
    

class Voke(db.Model):
    '''
        点赞表
    '''
    __tablename__ = 'voke'
    id = db.Column(db.Integer, primary_key=True)
    # 关系:一(User)对多(Voke)的关系
    user_id=db.Column(db.Integer,db.ForeignKey('user.ID'))
    # 关系:一(Topic)对多(Voke)的关系
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))

    def __init__(self,id):
        self.id = id

    def __repr__(self):
        return f'<User:{self.id}>'
    
 
class Category(db.Model):
    '''
        文章分类
    '''
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    cate_name=db.Column(db.String(50),nullable=False)
    # 定义与Topic的关联关系和反向引用
    topics = db.relationship('Topic',backref='category',lazy='dynamic')


    def __init__(self,cate_name):
        self.cate_name = cate_name

    def __repr__(self):
        return f'<User:{self.cate_name}>'


class Blogtype(db.Model):
    '''
        文章类型
    '''
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(20),nullable=False)
    # 增加与Topic之间的关联属性和反向引用关系
    topics = db.relationship('Topic',backref='blogtype',lazy='dynamic')

    def __init__(self,type_name):
        self.type_name = type_name

    def __repr__(self):
        return f'<User:{self.type_name}>' 


class Reply(db.Model):
    '''
        文章回复
    '''
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    # 关系:一(Topic)对多(Reply)的关系
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))
    # 关系:一(User)对多(Reply)的关系
    user_id = db.Column(db.Integer,db.ForeignKey('user.ID'))

    def __init__(self,type_name):
        self.type_name = type_name

    def __repr__(self):
        return f'<User:{self.type_name}>' 