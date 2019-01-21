from django.contrib import admin
from .models import *



# Register your models here.


class CarImgInline(admin.TabularInline):
    """设置多表在一表中的直接进行管理的类"""
    model = CarImg
    extra=1

# class CarInfoInline(admin.TabularInline):
#     model = CarInfo
#     extra=1


@admin.register(CarInfo)
class CarInfoAdmin(admin.ModelAdmin):
    """
        汽车信息管理类
    """
    # 设置显示在后台的字段
    list_display = (
        'brand',
        'model_number',
        'color',
        'regist_data',
        'mileage',
        'car_type',
        'place',
        'price',
        'newprice',
        'effluent_standard',
        "content",
        # 'created_updated_time',
        'isLegal',
        'isDelete'
    )
    
    #注意：必须设置字段为list_dispaly,设置排序方式
    ordering = ("-id",)


    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('brand','model_number')

    # 设置过滤器过滤的字段
    list_filter = ("brand", 'created_updated_time') 

    # 设置分层筛选字段　
    date_hierarchy = 'created_updated_time' 

    # 设置以及管理界面的便捷直接编辑字段,不可与 list_display_links相重合  
    list_editable = [
        'price',
        'isDelete'
    ]
    #Inline把BillSubInline关联进来,在主表中编辑多表的设置
    inlines = [
        CarImgInline,
    ]




@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
        汽车品牌信息管理类
    """
    list_display = ("title",'isDelete')#注意：必须设置字段为list_dispaly
    ordering = ("id",)
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('title',)
    list_editable = [
        'isDelete'
    ]
    # inlines = [
    #     CarInfoInline,
    # ]


# 自定义后台名称
admin.site.site_header = '优骏二手车汽车信息管理系统'
admin.site.site_title = '汽车信息管理'