from django.db import models
# Create your models here.

class GoodsType(models.Model):
    """
        商品类型
    """
    title = models.CharField('名称',max_length=30)
    desc = models.CharField('描述',max_length=200)
    picture = models.ImageField('照片',upload_to='static/images/good_type',default='normal.png')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods_type'
        verbose_name_plural = '商品分类'

class Goods(models.Model):
    '''
        商品表
    '''
    title = models.CharField('名称',max_length=30)
    price = models.IntegerField('价钱',null=False)
    unit = models.CharField('单位',max_length=20,default='500g')
    picture = models.ImageField('照片',upload_to='static/images/good',default='normal.png')
    desc = models.CharField('描述',max_length=200)
    detail = models.TextField('详情',max_length=1000)
    isDelete = models.BooleanField(default=False)
    goodtype = models.ForeignKey(GoodsType,on_delete=models.CASCADE)
    