-- 创建表 hero 和 sanguo
    -- create database MOSHOU;
    -- use MOSHOU;
    -- create table hero(id int,name char(15),sex enum("男","女"),country char(10))default charset=utf8;
    -- insert into hero values(1,"曹操","男","魏国"),(2,"小乔","女","吴国"),
    -- (3,"诸葛亮","男","蜀国"),(4,"貂蝉","女","东汉"),(5,"赵子龙","男","蜀国"),(6,"魏延","男","蜀国");
    -- create table sanguo(id int,name char(20),gongji int,fangyu tinyint unsigned,
    -- sex enum("男","女"),country varchar(20))default charset=utf8;
    -- insert into sanguo values
    -- (1,'诸葛亮',120,20,'男','蜀国'),
    -- (2,'司马懿',119,25,'男','魏国'),
    -- (3,'关羽',188,60,'男','蜀国'),
    -- (4,'赵云',200,66,'男','魏国'),
    -- (5,'孙权',110,20,'男','吴国'),
    -- (6,'貂蝉',666,10,'女','魏国'),
    -- (7,null,1000,99,'男','蜀国'),
    -- (8,'',1005,88,'女','蜀国');

-- 示意定位删除
    -- delete from hero where id = 6;
    -- delete from hero where name = "小乔" and country = "吴国";
    -- insert into hero values(6,"魏延","男","蜀国");
    -- insert into hero values(2,"小乔","女","吴国");
    -- update hero set  country = "蜀国" where id = 5;

-- 对hero进行定位where查询
    -- select * from hero where country="蜀国";
    -- select name,sex,country from hero where sex="女";
    -- update hero set  name="典韦",sex="男",country = "魏国" where id = 2;
    -- delete from hero where country = "蜀国";
    -- update hero set  country = "蜀国" where name = "貂蝉";
    -- delete from hero;

-- 对sanguo进行多条件查询
    -- select name,gongji from sanguo where gongji>200 and country = "蜀国";
    -- update sanguo set  gongji=100,fangyu=60 where gongji = 110;
    -- select * from sanguo where country ="魏国" or country="蜀国";
    -- select * from sanguo where gongji between 100 and 200 and country = "蜀国";
    -- select * from sanguo where country not in ("蜀国","魏国") and sex = "女";
    -- select * from sanguo where id in (1,3,5) and country="蜀国" or name = "貂蝉";

-- 示意NULL和空字符的区别
    -- select * from sanguo where name is NULL and country="蜀国" and sex = "男";
    -- select * from sanguo where name = "" and country="蜀国" and sex = "女";

-- 示意模糊查询
    -- select name from sanguo where name like "_%_";

-- 示意Order by 的排序用法
    -- select * from sanguo order by fangyu desc;
    -- select * from sanguo where country = "蜀国" order by gongji desc;
    -- select * from sanguo where country in ("蜀国","魏国") and name like "___" order by fangyu;

-- 示意limit的用法
    -- select * from sanguo where country="蜀国" order by fangyu limit 1,3;
    -- select name,gongji,country from sanguo where country="蜀国" order by gongji desc limit 3;

-- 示意聚合函数的用法
    -- select name,max(gongji) as 攻击力 from sanguo;
    -- select sum(gongji) as 攻击力总和 from sanguo; 
    -- select count(*) from sanguo;  任意字段只要有数据即可被计数   
    -- select count(*)  from sanguo where gongji>200 and country = "蜀国";

-- 示意分组和聚合函数的综合使用
    -- select country,avg(gongji) from sanguo group by country;
    -- select country,count(*) from sanguo where sex = "男" group by country order by count(*) desc limit 2;
    -- select country,avg(gongji) from sanguo group by country having avg(gongji)>105 order by avg(gongji) desc limit 2;    
    -- having 能对聚合函数进行过滤

-- 示意运算
    -- select name,gongji*2 from sanguo;

-- 示意子查询用法
-- 攻击值小于平均攻击值的英雄名字和攻击值查询出来
    -- 查询出平均值
        -- select avg(gongji) from sanguo;
    -- 找小于平均值的
        -- select name,gongji from sanguo where gongji < (select avg(gongji) from sanguo);
-- 找出每个国家的攻击力最高的英雄的名字和攻击值
-- select max(gongji) from sanguo group by country
    -- select name,gongji from sanguo where gongji in (select max(gongji) from sanguo group by country);
    