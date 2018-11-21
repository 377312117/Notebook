# 导入路径函数匹配相对应的地址
from django.urls import path
# 导入本应用的视图模块进行连接
from . import views





urlpatterns = [
    # 无后缀匹配该视图的book类
    path('',views.book),
    # 相应后缀匹配相应的类,与主应用的book/进行拼接
    path('detail/<book_id>/',views.book_detail)
]
