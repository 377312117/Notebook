from django.db import models
from userinfo.models import UserInfo,Address
from memberapp.models  import Goods
# Create your models here.

ORDERSTATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'订单取消'),
)

class Cart(models.Model):
    """
        购物车
    """
    user = models.ForeignKey(UserInfo,db_column='user_id',on_delete=models.CASCADE)
    # 与商品的外键
    good = models.ForeignKey(Goods,db_column='good_id',on_delete=models.CASCADE)
    ccount = models.IntegerField('数量',db_column='cart_count')

    def __str__(self):
        return self.user.uname

    class Meta:
        db_table = 'cartinfo'
        verbose_name_plural = '购物车'

class Order(models.Model):
    '''
        订单表
    '''
    user = models.ForeignKey(UserInfo,db_column='user_id',on_delete=models.CASCADE)
    orderNO = models.CharField('订单编号',max_length=30)
    acot = models.CharField('数量',max_length=200)
    aprice = models.CharField('价格',max_length=200)
    ads = models.CharField('收件人',max_length=200)
    cals = models.TextField('订单详情',null=True,blank=True)

    orderStatus = models.IntegerField('订单状态',blank=True,choices=ORDERSTATUS,default=1)

    def __str__(self):
        return self.user.uname
    
    def get_orderStatusDisplay(self):
        if self.orderStatus == 1:
            return u'未支付'
        elif self.orderStatus == 2:
            return u'已支付'
        elif self.orderStatus == 3:
            return u'订单取消'
        else:
            return u''

    class Meta:
        db_table = 'order'
        verbose_name_plural = '订单'