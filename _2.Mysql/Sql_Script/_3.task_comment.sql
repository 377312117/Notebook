
-- use studb2;
-- create table comment (comment_id int,article_id int,user_id int,date1 datetime);
-- insert into comment values(1,10000,10000,"2018-01-30 09:00:00");
-- insert into comment(comment_id,article_id,user_id) values(2,10001,10001);
-- insert into comment(comment_id,article_id,user_id) values(3,10002,10000);
-- insert into comment(comment_id,article_id,user_id) values(4,10003,10015);
-- insert into comment(comment_id,article_id,user_id) values(5,10004,10006);
-- insert into comment(comment_id,article_id,user_id) values(6,10025,10006);
-- insert into comment(comment_id,article_id,user_id) values(7,10009,10000);

-- 使用sql语句找出本站发表的所有评论数量最多的的前10位用户及评论数,并按评论数从高到低排序
    -- select user_id,count(user_id) from comment group by user_id order by count(user_id) desc limit 10;