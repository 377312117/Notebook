from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
# session 会话
from sqlalchemy.orm import sessionmaker

# 创建数据库连接对象
engine = create_engine("mysql+pymysql://root:123456@localhost/studb2")

# 创建ORM基类
Base = declarative_base()

# 创建session会话对象
session = sessionmaker(engine)()

# 继承Base
class User(Base):
    __tablename__ = "t123"
    id = Column(Integer,primary_key= True)
    name = Column(String(20))
    phnumber = Column(String(11),unique = True)

    #添加表记录
    def add_data(self):
        p = User(id = 1, name = "Lucy", phnumber = "13838383838")
        session.add(p)
    
    #查询表记录
    def select_data(self):
        result = session.query(User).filter_by(id = 1).all()
        for r in result:
            print(r.id,r.name)

# 提交到数据库执行
Base.metadata.create_all(engine)

if __name__ =="__main__":
    s = User()
    s.add_data()
    s.select_data()