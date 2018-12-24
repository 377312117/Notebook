from django.db import models

# Create your models here.

# 包含字段:
# 出版社名称name-varchar,
# address:出版社地址-varchar,
# city:出版社所在城市-varchar,
# country:出版社所在国家-varchar,
# website:出版社网址-varchar.

class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社名')
    address = models.CharField(max_length=200,verbose_name='地址')
    city = models.CharField(max_length=50,verbose_name='所在城市')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(verbose_name='网址')
    class Meta:
        # 指定表名
        db_table = 'Publisher'
        # 指定在admin的实体类名(单数)
        verbose_name_plural = '出版社'
    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    isActive = models.BooleanField(default=True,verbose_name='激活')
    class Meta:
        # 指定表名
        db_table = 'author'
        # 指定在admin的实体类名(单数)
        verbose_name_plural = '作者'
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name='书籍名')
    publicate_date = models.DateField(verbose_name='出版日期')
    # 添加外键
    publisher = models.ForeignKey(Publisher,null=True,on_delete=models.CASCADE)
    # 多表外键
    author_set = models.ManyToManyField(Author,null=True)
    class Meta:
        # 指定表名
        db_table = 'book'
        # 指定在admin的实体类名(单数)
        verbose_name_plural = '书籍'
    def __str__(self):
        return self.title
    
class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author = models.OneToOneField(Author,on_delete=models.CASCADE)


class Users(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    uemail = models.EmailField()