from django.shortcuts import render
from .models import Grades
from .models import Students

# Create your views here.

from django.http import HttpResponse

def  index(request):
    '''输入域名直接返回主页'''
    return HttpResponse('have a good day')

def detail(request,num):
    return    HttpResponse('detail-%s' % num)


def grades(request):
    '''从模型拿数据'''
    gradesList = Grades.objects.all()
    # 将数据传递给模板,再讲渲染好的页面返回浏览器
    return render(request,'MyApp/grades.html',{'grades':gradesList})


def students(request):
    '''从students模板拿数据'''
    studentsList = Students.objects.all()
    # 将数据传递给模板,再讲渲染好的页面返回浏览器
    return render(request,'MyApp/students.html',{'students':studentsList})

def gradeStudents(request,num):
    '''获得对应的班级对象'''
    grade = Grades.objects.get(pk=num)
    # 获得班级下的所有学生列表
    studentsList = grade.students_set.all()
    return render(request,'MyApp/students.html',{'students':studentsList})