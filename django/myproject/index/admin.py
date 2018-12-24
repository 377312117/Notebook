from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    # 定义在表单页显示的属性们
    list_display = ['name','age','email']
    # 定义允许被点击的字段们
    list_display_links = ['name','email']
    # 定义允许被修改的字段们
    list_editable = ['age']
    # 添加允许被搜索的字段们
    search_fields = ['name','email']
    # 右侧增加过滤器
    list_filter = ['name','email']
    # 在列表页顶部增加时间选择器,取值必须为DateField/DateTimeField
    # date_hierarchy
	# 作用
	# 	在列表页顶部增加时间选择器,
	# 取值
	# 	取值必须为DateField/DateTimeField
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Wife)