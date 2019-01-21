from django.apps import AppConfig
import os
 
 

# 修改后台管理中组的显示名称
default_app_config = 'carinfo.PrimaryBlogConfig'
 
VERBOSE_APP_NAME = u"1-汽车信息管理"
 
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
 
class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME




