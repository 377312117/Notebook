-- use studb2;
-- create table sheng(
-- id int primary key auto_increment,
-- s_id int,
-- s_name varchar(15)
-- )default charset=utf8;

-- insert into sheng values
-- (1, 130000, '河北省'),
-- (2, 140000, '陕西省'),
-- (3, 150000, '四川省'),
-- (4, 160000, '广东省'),
-- (5, 170000, '山东省'),
-- (6, 180000, '湖北省'),
-- (7, 190000, '河南省'),
-- (8, 200000, '海南省'),
-- (9, 200001, '云南省'),
-- (10,200002,'山西省');

-- create table city(
-- id int primary key auto_increment,
-- c_id int,
-- c_name varchar(15),
-- cfather_id int
-- )default charset=utf8;

-- insert into city values
-- (1, 131100, '石家庄市', 130000),
-- (2, 131101, '沧州市', 130000),
-- (3, 131102, '廊坊市', 130000),
-- (4, 131103, '西安市', 140000),
-- (5, 131104, '成都市', 150000),
-- (6, 131105, '重庆市', 150000),
-- (7, 131106, '广州市', 160000),
-- (8, 131107, '济南市', 170000),
-- (9, 131108, '武汉市', 180000),
-- (10,131109, '郑州市', 190000),
-- (11,131110, '北京市', 320000),
-- (12,131111, '天津市', 320000),
-- (13,131112, '上海市', 320000),
-- (14,131113, '哈尔滨', 320001),
-- (15,131114, '雄安新区', 320002);


-- create table xian(
-- id int primary key auto_increment,
-- x_id int,
-- x_name varchar(15),
-- xfather_id int
-- )default charset=utf8;

-- insert into xian values
-- (1, 132100, '正定县', 131100),
-- (2, 132102, '浦东新区', 131112),
-- (3, 132103, '武昌区', 131108),
-- (4, 132104, '哈哈', 131115),
-- (5, 132105, '安新县', 131114),
-- (6, 132106, '容城县', 131114),
-- (7, 132107, '雄县', 131114),
-- (8, 132108, '嘎嘎', 131115);

-- 此示例示意多表查询
-- 1.查询省,市详细信息
    -- 河北省 石家庄市
    -- 河北省 廊坊市
    -- 河北省 武汉市
        -- select sheng.s_name,city.c_name from sheng,city where sheng.s_id = city.cfather_id;
-- 2.查询省市县的详细信息
    -- select sheng.s_name,city.c_name,xian.x_name from sheng,city,xian 
    -- where sheng.s_id = city.cfather_id and city.c_id = xian.xfather_id;

-- 此示例示意连接查询
    -- 内连接
    -- 查找省,市详细信息
        -- select sheng.s_name,city.c_name,xian.x_name from sheng inner join city on 
        -- sheng.s_id = city.cfather_id inner join xian on city.c_id = xian.xfather_id;
    -- 外连接
    -- 左连接
        -- select sheng.s_name,city.c_name,xian.x_name from sheng left join city on 
        -- sheng.s_id = city.cfather_id left join xian on city.c_id = xian.xfather_id;
    -- 右连接
select sheng.s_name,city.c_name,xian.x_name from sheng right join city on 
sheng.s_id = city.cfather_id right join xian on city.c_id = xian.xfather_id;    