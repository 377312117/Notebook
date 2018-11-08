-- create table t5(id int not null,name varchar(20),age tinyint,phnumber char(11),cardnumber int,
-- index(name),index(age),unique(phnumber),unique(cardnumber));

-- create unique index x on t5(id);

-- drop index x on t5;

-- 此示例示意外键约束
-- use studb2;
-- create table payment(id int primary key,name varchar(20) not null,class char(5) default "AID",money smallint)
-- charset = utf8;

-- insert into payment values(1,"唐伯虎","AID08",300),(2,"秋香","AID08",200);
create table class(stu_id int primary key,name varchar(20),money smallint,foreign key (stu_id) references payment(id)
on delete cascade on update cascade);