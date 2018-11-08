from mysqlpython import Mysqlpython

sqlh = Mysqlpython("studb2")
dele = "delete from t2 where name='杜牧'"
sqlh.zhixing(dele)