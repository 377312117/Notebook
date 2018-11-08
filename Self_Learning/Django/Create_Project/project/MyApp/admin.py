from django.contrib import admin

# Register your models here.

from .models import Grades,Students


# 注册
class StudentsInfo(admin.TabularInline):  # Stackedlnline
    '''为student表添加页面进行修改'''
    model = Students
    extra = 2



class GradesAdmin(admin.ModelAdmin):
    '''对班级表的管理页面进行修改'''
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk','gname','gdate','ggirlnum']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # 添加修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    # fieldsets = [
        # ('num':{fields:['ggirlnum','gboynum']}),('base',
        # {"fields":['gname','gdate','isDelete']}),
    # ]
    
# 执行该命令,对页面进行自定义
admin.site.register(Grades,GradesAdmin)

# 装饰器装饰,更为简洁方便
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    '''对student管理页面进行修改'''
    def gender(self):
        '''对应男女显示性别的问题'''
        if self.sgender:
            return '男'
        else:
            return '女'
    # 设置页面列的名称
    gender.short_description = '性别'
    # 列表页属性
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 10
    # 执行动作的位置
    actions_on_top = False   # 在页面上方,True为上方,默认在上方
    actions_on_bottom = True # 在页面下方,设置True在下面


# admin.site.register(Students,StudentsAdmin)
