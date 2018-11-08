from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$',views.detail),
    # 组里的数字给了views.py.detail函数的num中

    url(r'^grades/$',views.grades),
    url(r'^students/$',views.students),
    url(r'^grades/(\d+)$',views.gradeStudents)
]