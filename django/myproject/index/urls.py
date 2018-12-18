from django.conf.urls import url
from .views import *

urlpatterns = [
    # 当访问路径为index/的时候,将请求交给index_views视图函数去处理,完整请求格式为
    # ht..../music/index
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^$',index_views),
    url(r'01-temp/$',temp_views),
    url(r'02-temp/$',temp02_views),
    url(r'03-var/$',var_views), 
    url(r'04-static/$',static_views), 
]