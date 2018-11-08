# 用字符串"ABC"和＂123＂生成如下列表
# ［＂A1＂,"A2""A3""B1""B2""""...］
l1=[x+y for x in "ABC" for y in "123"]
print(l1)