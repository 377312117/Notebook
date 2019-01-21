from django.db import models

# Create your models here.


COLOR_CHOICE=(
    (0,'黑色'),
    (1,'白色'),
    (2,'红色'),
    (3,'蓝色'),
    (4,'银灰色'),
    (5,'紫色'),
)

EFFLUENT_CHOICE=(
    (0,'国一'),
    (1,'国二'),
    (2,'国三'),
    (3,'国四'),
    (4,'国五'),
    (5,'国六'),
)

MODEL_CHOICE=(
    (0,'小型车'),
    (1,'紧凑经济型'),
    (2,'中型'),
    (3,'中大型车'),
    (4,'豪华车'),
)


class Brand(models.Model):
    """
        品牌信息类
    """
    title = models.CharField('名称',max_length=50,null=False)
    logo = models.ImageField('logo',upload_to='img/logo',default='')
    isDelete=models.BooleanField('是否有效',default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='品牌信息'
        verbose_name_plural='品牌信息'


class CarInfo(models.Model):
    """
        品牌信息类
    """
    brand=models.ForeignKey(Brand,verbose_name='汽车品牌', on_delete=models.CASCADE)
    model_number = models.CharField('型号',max_length=200)
    color = models.IntegerField('颜色',choices=COLOR_CHOICE,default=0)
    regist_data = models.DateField('上牌日期')
    mileage = models.IntegerField('公里数')
    car_type = models.IntegerField('车型',choices=MODEL_CHOICE,default=1)
    place = models.CharField('上牌地',max_length=200)
    price = models.DecimalField('期望成交价格',max_digits=8,decimal_places=2)
    newprice = models.DecimalField('新车价格',max_digits=8,decimal_places=2)
    effluent_standard = models.IntegerField('排放标准',choices=EFFLUENT_CHOICE,default=4)
    content = models.TextField('汽车详情')
    created_updated_time = models.DateTimeField('汽车上架时间',auto_now = True)
    isLegal = models.BooleanField('是否为正规渠道车辆',default=True)
    isDelete = models.BooleanField("是否在售",default=True)

    def __str__(self):
        return self.model_number
    
    class Meta:
        verbose_name='汽车信息'
        verbose_name_plural='汽车信息'


    
class CarImg(models.Model):
    """
        汽车图片类
    """
    car = models.OneToOneField(CarInfo,verbose_name='汽车型号',on_delete=models.CASCADE,null=False)
    img1 =models.ImageField('封面图片',upload_to='img/car')
    img2 =models.ImageField('细节图片1',upload_to='img/car')
    img3 =models.ImageField('细节图片2',upload_to='img/car')
    img4 =models.ImageField('细节图片3',upload_to='img/car')
    img5 =models.ImageField('细节图片4',upload_to='img/car')
    img6 =models.ImageField('细节图片5',upload_to='img/car')
    isDelete = models.BooleanField("是否保存图片信息",default=True)
    

    def __str__(self):
        return self.car.model_number
    
    class Meta:
        verbose_name='汽车图片'
        verbose_name_plural='汽车图片'
