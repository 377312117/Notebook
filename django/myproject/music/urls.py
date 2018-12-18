from django.conf.urls import url
from .views import index_views

urlpatterns = [
    # 当访问路径为index/的时候,将请求交给index_views视图函数去处理,完整请求格式为
    # ht..../music/index
    url(r'^$',index_views)
]
