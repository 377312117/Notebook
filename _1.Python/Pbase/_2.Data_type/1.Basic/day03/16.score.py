# 输入三科成绩，打印最高，最低，平均成绩
a=float(input("请输入数学成绩："))
b=float(input("请输入英语成绩："))
c=float(input("请输入语文成绩："))
# avg=(math+english+chinese)/3
# if  math<english:
#     if math>=chinese:
#         print("最高成绩是:%d"%english)
#         print("最低成绩是:%d"%chinese)
#         print("平均成绩是:%d"%avg)
#     elif math<chinese<=english:
#         print("最高成绩是:%d"%english)
#         print("最低成绩是:%d"%math)
#         print("平均成绩是:%d"%avg)
#     else:
#         print("最高成绩是:%d"%chinese)
#         print("最低成绩是:%d"%math)
#         print("平均成绩是:%d"%avg)
# else:
#     if chinese<=english:
#         print("最高成绩是:%d"%math)
#         print("最低成绩是:%d"%chinese)
#         print("平均成绩是:%d"%avg)     
#     elif chinese>=math:
#         print("最高成绩是:%d"%chinese)
#         print("最低成绩是:%d"%english)
#         print("平均成绩是:%d"%avg) 
#     else:
#         print("最高成绩是:%d"%math)
#         print("最低成绩是:%d"%english)
#         print("平均成绩是:%d"%avg) 
maxs=a
if b>maxs:
    maxs=b
if c>maxs:
    maxs=c 
print(maxs)