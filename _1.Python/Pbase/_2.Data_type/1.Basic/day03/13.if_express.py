#此例子示例条件表达式语法
#商品促销满１００－２０
money=int(input("请输入商品总额："))
pay=money-20 if money>=100 else money
print("您需要支付%d元"%pay)
