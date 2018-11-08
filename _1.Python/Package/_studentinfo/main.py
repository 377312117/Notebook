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
#主程序
from menu import show_menu
from addinfo import input_studentinfo
from print_info import print_studentinfo
from del_info import delete_studentinfo
from del_info import delete_studentinfo
from modify_info import alter_studentscore
from select_info import print_score_desc
from select_info import print_score_asc
from select_info import print_age_desc
from select_info import print_age_asc
from infos_read import read_from_file
from infos_save import save_to_file
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
            infos = save_to_file()
        elif s == 'q':
            print("已退出系统!")
            break
main() 