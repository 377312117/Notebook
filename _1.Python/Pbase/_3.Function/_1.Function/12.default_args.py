#此示例示意函数的缺省参数
def info(name,age=1,address="不详"):
    print(name,"今年",age,"岁","家庭住址:",address)
info("魏明择",35,"北京市朝阳区")
#返回:魏明哲今年35岁,家庭住址:北京市朝阳区
info("tarena",16)
#返回:当有缺省参数时,可不给参数,然后输出默认参数