-- use studb2;
-- create table score(id int,name varchar(20),score float(5,2),phnumber char(11),class char(7))
-- charset = utf8;

-- 示意 数据导入
-- load data infile "/var/lib/mysql-files/scoreTable.csv" into table score
-- fields terminated by "," lines terminated by "\n";

-- 示意 数据导出
-- 把MOSHOU库下的sanguo表的英雄的姓名,攻击值和国家导出到sanguo.csv
        -- use MOSHOU;
        -- select * from sanguo
        -- into outfile "/var/lib/mysql-files/sanguo.csv"
        -- fields terminated by ","
        -- lines terminated by "\n";