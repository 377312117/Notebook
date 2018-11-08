from django.db import models

# Create your models here.

class Grades(models.Model):
    '''对应数据库上的班级表,属性会对应表里的字段'''
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        # 返回女孩名
        return self.gname

class Students(models.Model):
    '''对应数据库中的学生表'''
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE)
    
    def __str__(self):
        # 返回名称
        return self.sname