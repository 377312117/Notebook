#改写之前的学生信息管理系统
# #要求添加四个功能:
# 5)按学生成绩从高到低排列学生信息
# 6)按学生成绩从低到高排列学生信息
# 7)按学生年龄从高到低排列学生信息
# 8)按学生年龄从低到高排列学生信息

#实现带界面的学生信息管理系统的项目
#+--------------------------+
#|1)添加学生信息              |
#|2)显示学生信息              |
#|3)删除学生信息              |
#|4)退出                     |
#+--------------------------+
# 用函数来实现,每个功能写一个函数与之相对应

# 导入模块
from menu import show_menu
from student_info import *

# 主程序
def main():
    infos=[]
    while True:
        show_menu()
        s=input("请输入选项:")
        if s == '1':
            infos += input_studentinfo()
        elif s == '2':
            print_studentinfo(infos)
        elif s == '3':
            delete_studentinfo(infos)
        elif s == '4':
            alter_studentscore(infos)
        elif s == '5':
            print_score_desc(infos)
        elif s == '6':
            print_score_asc(infos)
        elif s == '7':
            print_age_desc(infos)
        elif s == '8':
            print_age_asc(infos)
        elif s == '9':
            infos = read_from_file()
        elif s == '10':
            save_to_file(infos)
        elif s == 'q':
            print("已退出系统!")
            break
main() 