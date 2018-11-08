-- use studb2;
-- create table userinfo(u_name varchar(20),u_passwd varchar(10),u_uid int,u_gid int,
-- u_des varchar(20),u_route varchar(50),u_right varchar(50));


-- load data infile "/var/lib/mysql-files/passwd" into table userinfo
-- fields terminated by ":" lines terminated by "\n";

-- 新增id列后添加主键和自增长属性
-- alter table userinfo add id int(3) Zerofill primary key auto_increment first;

