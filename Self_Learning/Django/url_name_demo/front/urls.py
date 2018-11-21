from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    # path有个参数name,可以为url取名,
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]