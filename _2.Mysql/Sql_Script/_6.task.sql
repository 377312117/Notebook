-- 创建customers表
    -- use studb2;
    -- create table customers(c_id int primary key auto_increment,c_name varchar(20),
    -- c_age tinyint unsigned,c_sex enum("M","F"),c_city varchar(20),c_salary double(12,2));
    -- insert into customers values
    -- (1,"Zhangsan",25,"M","Beijing",8000),
    -- (2,"Lisi",30,"F","Shanghai",10000),
    -- (3,"Wangwu",27,"M","Shenzhen",12000);

-- 创建orders表
    -- create table orders(o_id int,o_name varchar(20),o_price double(12,2),
    -- foreign key (o_id) references customers(c_id)on delete cascade on update cascade);
    -- insert into orders values
    -- (1,"iphone",5288),
    -- (1,"ipad",3299),
    -- (3,"mate9",3688),
    -- (2,"iwatch",2222),
    -- (2,"r11",4400);

-- 返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
    -- select * from customers where c_salary>4000 or c_age<29  limit 2;

-- 把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
    -- select c_name,c_salary*1.15 from customers where c_age>25 or c_city in ("Beijing","Shanghai");

-- 把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
    -- select * from customers where  c_city ="Beijing" order by c_salary desc limit 1;

-- 选择工资c_salary最少的顾客的信息
    -- select * from customers where c_salary = (select min(c_salary) from customers);

-- 找到工资大于5000的顾客都买过哪些产品的记录明细
    -- select c_name,o_name from customers,orders where c_id = o_id and c_salary> 5000;

-- 删除外键
    -- show create table orders;
    -- alter table orders drop foreign key orders_ibfk_1;

-- 删除customers主键限制
    -- 1、删除自增长属性
    -- 2、删除主键限制
    -- alter table customers modify c_id int;
    -- alter table customers drop primary key;