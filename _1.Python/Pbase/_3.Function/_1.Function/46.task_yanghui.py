#写程序打印杨辉三角(只打印6层)
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1
# sn[m]=s(n-1)[m-1]+s(n-1)[m]

#创建阶乘函数,便于下面的语句中调用
# def myseq(m):
#       seq=1
#       for x in range(1,m+1):
#             seq*=x
#       return seq
# def tri(n):
# #下列循环是典型的生成有序序列的组合
#       for i in range(1,n+1):
#             for j in range(1,i+1):
# #通项公式:C(i,j)=C(i-1)!/(C(j-1)*C(i-j))
# #难点在于要怎么将公式进行处理,
# # 然后生成有序序列,将公式带入到你要生成的循环之中
#                   print(int(myseq(i-1)/(myseq(j-1)*myseq(i-j))),end=" ")
#             print()
# tri(6)

# 方法2
#1.制造相应的列表
def get_next_list(L):
      #用给定的一行L,返回下一行
      #如L为[1,2,1],则返回[1,3,3,1]
      rl =[1]
      # 算中间的数字(循环获取从零开始的索引)
      for i in range(len(L)-1):
            v=L[i]+L[i+1]
            rl.append(v)
      rl.append(1)  #最右边的1
      return rl
# print(get_next_list(1,2,1))
# 2.生成全部的行放到一个整体的列表中
def yh_list(n):
      # 如果n为3,返回的列表是:
      # [[1],[1,1],[1,2,1]]
      rl=[]
      L=[1]
      while len(rl)<n:
            rl.append(L)
            L=get_next_list(L)
            #计算出下一行
      return rl
# print(yh_list(6))    测试
#第三步:把杨辉三角的列表转为字符串列表
def get_yh_string(L):
      rl=[]
      for line in L:
            # line = [1,2,1] -->s= "1 2 1"
            str_list = [str(x) for x in line]
            s = " ".join(str_list)
            rl.append(s)
      return rl
# 第四步,打印杨辉三角
def print_yh_triangle(L):
      max_len=len(L[-1])
      for s in L:
            print(s.center(max_len))
L=yh_list(6)
SL=get_yh_string(L)
print_yh_triangle(SL)
