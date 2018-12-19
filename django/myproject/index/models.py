from django.db import models

# Create your models here.

# 包含字段:
# 出版社名称name-varchar,
# address:出版社地址-varchar,
# city:出版社所在城市-varchar,
# country:出版社所在国家-varchar,
# website:出版社网址-varchar.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
