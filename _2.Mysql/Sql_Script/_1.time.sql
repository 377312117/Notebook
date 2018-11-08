-- 插入t8表数据,并示例函数的用法
-- 先切换到指定数据库
use studb2;
-- 创建表
-- create table t8(id int,username varchar(20),password varchar(20),money int,birthday date,cztime timestamp) ;
-- 插入数据
insert into t8 values(1,"用户1","123456",300,"1985-03-03",now());
insert into t8 values(2,"用户2","123456",500,"1985-03-03","2018-10-8 11:00:00");
insert into t8 values(3,"用户3","123456",700,"1985-03-03","2017-10-7 11:00:00");
insert into t8 values(4,"用户4","123456",900,"1987-05-03","2018-10-5 13:00:00");
insert into t8 values(5,"用户5","123456",1100,"1989-05-03","2018-10-8 10:30:00");
insert into t8 values(6,"用户6","123456",1100,"1989-05-03","2018-10-8 10:30:00");
insert into t8 values(7,"用户7","123456",1300,"1989-06-03","2018-9-8 11:30:00");
insert into t8 values(8,"用户8","123456",1300,"1989-06-03","2018-9-30 11:30:00");
-- 示意time()等函数的用法
select * from t7 where time(cztime) between  "2018-10-08 10:00:00" and "2018-10-08 12:00:00" ;
select * from t7 where date(cztime) between  "2018-10-01" and "2018-10-31" ;
-- 示意   字段 >=(now()-interval 1 day)的用法
-- select * from t8 where cztime >=(now()-interval 1 day);
-- select * from t8 where cztime <=(now()-interval 1 year);
-- select * from t8 where cztime <=(now()-interval 1 day) and cztime >=(now()-interval 3 day);