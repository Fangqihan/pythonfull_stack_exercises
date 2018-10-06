
/***表结构：
        班级表:class
        学生表:student
        老师表:teacher
        课程表:course
        成绩表:score
        年级表：class_grade
        班级任职表：teach2cls
    **/

/***************************一、创建表结构***********************************/



drop table if EXISTS class_grade;
CREATE TABLE `class_grade` (
   `gid` int(11) NOT NULL AUTO_INCREMENT,
   `gname` varchar(20) COMMENT'年级',  
  PRIMARY KEY (`gid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='年级表';


drop table if EXISTS class;
CREATE TABLE `class` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(30)  COMMENT '班级名称',  
  `grade_id` int(11) COMMENT'年级',  
  PRIMARY KEY (`cid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='班级表';

CREATE INDEX idx_grade_id on class(grade_id);


drop table if EXISTS student;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20)  COMMENT '学生姓名',  
  `gender` char(2)  COMMENT '性别', 
  `class_id` int(11) COMMENT '班级ID', 
  PRIMARY KEY (`sid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='学生表';

CREATE INDEX idx_class_id  on student(class_id);


drop table if EXISTS teacher;
CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(20)  COMMENT '老师姓名',
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='老师表';


drop table if EXISTS course;

CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(20)  COMMENT '课程',
   tearch_id int(11) COMMENT'老师ID',
  PRIMARY KEY (`cid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程表';

CREATE INDEX idx_tearch_id  on course (tearch_id);


drop table if EXISTS score;
CREATE TABLE `score` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  student_id int(11) COMMENT'学生ID',
  course_id int(11) COMMENT'课程ID',
  score NUMERIC(4,1) COMMENT'分数',
 PRIMARY KEY (`sid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='成绩表';

CREATE INDEX idx_student_id  on score(student_id) ;
CREATE INDEX idx_course_id  on score(course_id) ;


drop table if EXISTS teach2cls;
CREATE TABLE `teach2cls` (
   `tcid` int(11) NOT NULL AUTO_INCREMENT,
   `tid` int(11) COMMENT'老师id',
   `cid`  int(11) COMMENT'班级id' ,
  PRIMARY KEY (`tcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='班级任职表';


CREATE INDEX idx_tid  on teach2cls(tid) ;
CREATE INDEX idx_cid on teach2cls(cid) ;



/************************二、添加测试数据*******************************/
 #插入数据
    insert into class_grade(gname) values    # 4个年级
    ('一年级'),
    ('二年级'),
    ('三年级'),
    ('四年级');


    insert into class(caption,grade_id) values  # 9个班级
    ('一年一班',1),
    ('一年二班',1),
    ('一年三班',1),
    ('二年一班',2),
    ('二年二班',2),
    ('三年一班',3),
    ('三年二班',3),
    ('四年一班',4),
    ('四年二班',4);


    insert into student(sname,gender,class_id) values  # 12个学生
    ('Jane','女',1),
    ('Rose','女',1),
    ('Jack','男',2),
    ('Alice','女',2),
    ('Alex','男',3),
    ('Drigon','男',4),
    ('Lily','女',5),
    ('Lucy','女',6),
    ('Jone','男',6),
    ('紫霞','女',7),
    ('张尊宝','男',8),
    ('高圆圆','女',9);



    insert into teacher(tname) values   # 4个老师
    ('曹显'),
    ('王浩'),
    ('王五'),
    ('赵坤');


    insert into course(cname,tearch_id) values  # 6门课程
    ('生物',1),
    ('物理',2),
    ('化学',3),
    ('语文',3),
    ('数学',4),
    ('地理',2);




    insert into score(student_id,course_id,score) values # 12个学生，6门课程
    (1,1,60),
    (1,2,59),
    (2,4,60),
    (2,5,59),
    (2,6,33),
    (3,1,59),
    (3,5,28),
    (4,4,100),
    (4,6,90),
    (5,4,88),
    (6,5,100),
    (6,6,60),
    (7,3,57),
    (7,5,60),
    (8,2,61),
    (8,4,59),
    (9,1,60),
    (9,2,61),
    (9,3,21),
    (10,5,68),
    (11,1,89),
    (12,3,100);


    insert into teach2cls(tid,cid) values # 4个老师 9个班级
    (1,1),
    (1,2),
    (1,3),
    (1,7),
    (2,4),
    (2,8),
    (2,7),
    (2,5),
    (3,9),
    (3,3),
    (3,5),
    (3,2),
    (4,8),
    (4,4),
    (4,6),
    (4,1);


/***************************************************三、SQL语句**************************************************************/
#2.查看学生总人数
SELECT count(*) from student;


#3.查询"生物"课程和"物理"课程成绩都及格的学生id和姓名



方式一：
select sid,sname 
from student
where sid in 
		(
		select student_id
		from score s 
		left join course c
		on s.course_id = c.cid
		where cname in ('生物','物理')
		and score >= 60
		group by student_id
		having count(*) >=2
		)

方式二：
SELECT
	A.student_id,
	c.sname
FROM
	(
		SELECT
			student_id,
			score AS sw
		FROM
			score
		LEFT JOIN course ON score.course_id = course.cid
		WHERE
			course.cname = '生物' and score>=60
	)AS A
INNER JOIN(


#LEFT JOIN
	SELECT
		student_id,
		score AS wl
	FROM
		score
	LEFT JOIN course ON score.course_id = course.cid
	WHERE
		course.cname = '物理' and score>=60
)AS B ON A.student_id = B.student_id
INNER JOIN student c
on a.student_id=c.sid;



#4.查询每个年级的班级数，取出班级数最多的前三个年级
方式一：
select grade_id, gname, count(*) cnt
from class c
left join class_grade g
on c.grade_id = g.gid
group by grade_id
having cnt >=(
							select count(*) cnt
							from class 
							group by grade_id
							ORDER BY cnt desc
							limit 3,3
							)

方式二：
SELECT a.grade_id,b.gname
from class a,class_grade b
where a.grade_id=b.gid
group by a.grade_id
ORDER BY count(*) desc 
LIMIT 3;


#5、查询平均成绩最高和最低的学生id和姓名以及平均成绩；   
 
select a.student_id,b.sname,a.score
from  
(select student_id,avg(score) score  from score group by student_id  ORDER BY  avg(score) desc LIMIT 1) a,student b
where a.student_id=b.sid
union all 
select a.student_id,b.sname,a.score
from  
(select student_id,avg(score) score  from score group by student_id  ORDER BY  avg(score)  LIMIT 1) a,student b
where a.student_id=b.sid;


#6.查询每个年级的学生人数


SELECT a.gname,count(c.sid)
from class_grade a
LEFT JOIN class b
on a.gid=b.grade_id
LEFT JOIN student c
on b.cid=c.class_id
group by a.gid;

#7.查询每位学生的学号,姓名,选课数,平均成绩

SELECT a.sid,a.sname,count(b.course_id) num_course,avg(b.score)
from student a
LEFT JOIN score b
on a.sid=b.student_id
group by a.sid;



#8.查询学生编号为“2”的学生的姓名，该学生成绩最高的课程名。成绩最低的课程名及分数


SELECT c.cname,b.score 
from score a,
(
SELECT max(score)  score from score
where student_id=2
union all 
SELECT min(score) from score
where student_id=2
) b,
course c
where a.score=b.score 
      and  a.course_id=c.cid
      and a.student_id = 2;


#9.查询姓“李”的老师个数和所带班级数
select count(distinct tt.tid), count(*)
from (
	select tid
	from teacher t
	where t.tname like '李%') tt
left join teach2cls tc
on tt.tid = tc.tid


#10 查询班级数小于5的年级id和 年级名

SELECT a.gid,a.gname
from class_grade  a
LEFT JOIN class b
on a.gid=b.grade_id
GROUP BY a.gid
HAVING count(*)<5;

#11  查询班级信息，包括班级id,班级名称，年级，年级级别（12为低年级，34为中年级，56为高年级


SELECT a.cid,a.caption,b.gname,
(case when b.gid<=2 then '低年级'
      when b.gid<=4 then '中年级'
      when b.gid<=6 then '高年级' end) as  '年级级别'
from class a ,class_grade b
where a.grade_id = b.gid;





#12查询学过“张三”老师2门课以上的同学的学号，姓名


select 
                student.sid,student.sname
            from 
                student
            where 
                sid in(
                    select 
                        student_id
                    from 
                        score
                    where
                        course_id in(
                            select    
                                course.cid
                            from
                                teacher,  
                                course  
                            where 
                                teacher.tid=course.tearch_id
                                and teacher.tname='张三'
                            )
                    group by
                        student_id
                    having
                        count(course_id) >2
                );

或：
select * from student 
where sid in 
	(select sc.student_id from score sc
	left join course c
	on sc.course_id = c.cid
	left join teacher t
	on c.tearch_id = t.tid
	where t.tname = '王五'
	group by sc.student_id
	having count(*) >2)


#13.查询教授课程超过2门的老师的id和姓名

select * from teacher t1 
where t1.tid in (
			select t.tid from teacher t
			left join course c
			on t.tid = c.tearch_id
			group by t.tid
			having count(*) >=2
			)


#14 查询学过编号1和编号2课程的同学的学号和姓名

select s.sid,s.sname
from student s 
left join score sc
on s.sid = sc.student_id
where sc.course_id in (1,2)
group by s.sid 
having count(*) >=2



#15、查询没有带过高年级的老师id和姓名；

方式一：
select tid,tname from teacher 
where tid not in
(
select t.tid
from teacher t
left join teach2cls tc
on t.tid = tc.tid
left join class c
on tc.cid = c.cid
where c.grade_id >=5
)

方式二：
SELECT e.tid,e.tname from teacher e
LEFT JOIN
(
SELECT a.tid from teach2cls a ,class b 
where a.cid=b.cid and grade_id>=5
)f
on e.tid=f.tid 
where f.tid is null; 



#16 查询学过“张三”老师所教的所有课的同学的学号 姓名

select * 
from student 
where sid in 
	(select sc.student_id
	from  score sc
	left join course c
	on sc.course_id = c.cid
	left join teacher t
	on c.tearch_id = t.tid
	where t.tname = '王五'
	group by sc.student_id
	having count(*)  >=
		(select count(*) from teacher t
		left join course c
		on t.tid = c.tearch_id
		where t.tname = '王五'
		)
	)


SELECT
	student_id,
	sname
FROM
	(
		SELECT
			student_id,
			course_id
		FROM
			score m,
			(
				SELECT
					cid
				FROM
					teacher a,
					course b
				WHERE
					tname = '张三'
				AND tid = b.tearch_id
			)n
		WHERE
			m.course_id = n.cid
	)AS B
LEFT JOIN student ON B.student_id = student.sid
GROUP BY
	student_id
HAVING
	count(student_id)=(
		SELECT
			count(cid)
		FROM
			teacher a,
			course b
		WHERE
			tname = '张三'
		AND tid = b.tearch_id
	);

#17.查询带过超过2个班级的老师id和姓名

select t.tid,t.tname from teacher t
inner join 
(select tc.tid from teach2cls tc
group by tc.tid
having count(*) >2
) c
on t.tid = c.tid


#18.查询课程编号 "2"的成绩比课程编号"2"课程低的所有同学的学号、姓名
SELECT a.sid,a.sname
from student a,
(
SELECT student_id,score  from score where  course_id=2) b,
(SELECT student_id,score  from score where  course_id=1) c
where  a.sid=b.student_id  and b.student_id=c.student_id and b.score<c.score; 

#19 查询所带班级数最多的老师id和姓名

SELECT
		t.tid, t.tname
from teacher t
left join teach2cls tc
on t.tid = tc.tid
GROUP BY t.tid,t.tname
having count(cid) >=
	(SELECT count(DISTINCT cid) num_class
		FROM teach2cls
		GROUP BY tid
		order by num_class desc
		limit 1)
		

#20、查询有课程成绩小于60分的同学的学号、姓名；

方式一：
select t.sid,t.sname from score s
left join student t
on s.student_id = t.sid
group by student_id
having min(score)<60

方式二：
SELECT a.sid,a.sname from student a
where EXISTS(
SELECT 1 from score
where score<60 and student_id=a.sid);

#21、查询没有学全所有课的同学的学号、姓名；

SELECT e.sid,e.sname
from student e,
(
SELECT student_id
from score
GROUP BY student_id
HAVING count(DISTINCT course_id)<(SELECT count(*) from course)
)f
where e.sid=f.student_id;


　#　22、查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；


 SELECT a.student_id,c.sname
 from score a,( SELECT course_id from score where sid=1)b,student c
 where a.course_id=b.course_id and a.student_id=c.sid
 GROUP BY a.student_id;



#　　23、查询至少学过学号为“1”同学所选课程中任意一门课的其他同学学号和姓名；

 SELECT a.student_id,c.sname
 from score a,( SELECT course_id from score where sid=1)b,student c
 where a.course_id=b.course_id and a.student_id=c.sid and a.student_id<>1
 GROUP BY a.student_id;



#　　24、查询和“2”号同学学习的课程完全相同的其他同学的学号和姓名;

SELECT
	student_id,
	sname
FROM
	score
LEFT JOIN student ON score.student_id = student.sid
WHERE#课程门数一样
	student_id IN(
		SELECT			student_id
		FROM			score
		WHERE			student_id != 2
		GROUP BY			student_id
		HAVING			count(course_id)=(SELECT count(1)	FROM	score	WHERE	student_id = 2)
	)
#且是一样课程
AND course_id IN(
	SELECT		course_id	FROM		score
	WHERE		student_id = 2
)
GROUP BY	student_id;



#　　25、删除学习“张三”老师课的score表记录；
delete from score where course_id in
(
select c.cid from course c
left join teacher t
on c.tearch_id = t.tid
where t.tname = '张三'
)

　#　26、向score表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“2”课程的同学学号；②插入“2”号课程的平均成绩；



   insert into score(student_id, course_id, score) 
   select a.sid,2,(select avg(score) 
                  from score where course_id = 2) 

    from student a LEFT JOIN score b 
    on a.sid=b.student_id and b.course_id = 2
    where b.student_id is null ;



　#　27、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；


    select a.student_id,
        sum(case when b.cname='语文' then a.score else 0 end ) as 语文,
        sum(case when b.cname='数学' then a.score else 0 end ) as 数学,
        sum(case when b.cname='英语'  then a.score else 0 end ) as 英语,
        count(a.course_id),
        avg(a.score)
    from score as a LEFT JOIN course b
    on a.course_id=b.cid
    group by a.student_id# desc    
    ORDER BY avg(a.score)  asc  ;



　#　28、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；


 select course_id, max(score) as max_num, min(score) as min_num from score group by course_id;



　#　29、按各科平均成绩从低到高和及格率的百分数从高到低顺序；



    select course_id, avg(score) as avgnum,sum(case when score.score > 60 then 1 else 0 END)/count(1)*100 as percent 
    from score 
    group by course_id 
    order by avgnum asc,percent desc;



　#　30、课程平均分从高到低显示（现实任课老师）；


    select teacher.tname,course.cname,avg(ifnull(score.score,0)) avg_num 
    from course 
    left join score on course.cid = score.course_id 
    left join teacher on course.tearch_id = teacher.tid
    group by score.course_id
    ORDER BY avg_num desc;



#　　31、查询各科成绩前三名的记录(不考虑成绩并列情况)
#方法一：  
  select score.sid,score.course_id,score.score,T.first_num,T.second_num,t.third_num 
    from score 
    left join
    (select
        sid,#s1.course_id,
        (select score from score as s2 where s2.course_id = s1.course_id order by score desc limit 0,1) as first_num,
        (select score from score as s2 where s2.course_id = s1.course_id order by score desc limit 1,1) as second_num,
        (select score from score as s2 where s2.course_id = s1.course_id order by score desc limit 2,1) as third_num
    from
        score as s1 #where course_id=2
    ) as T
    on score.sid =T.sid
    where score.score <= T.first_num and score.score >= T.third_num;

#方法二：

SELECT a.student_id, a.course_id, a.score FROM score AS a WHERE 
(SELECT COUNT(DISTINCT score) FROM score AS b 
WHERE b.course_id = a.course_id AND b.score >= a.score) <= 3 
ORDER BY a.course_id ASC, a.score DESC;


　#　32、查询每门课程被选修的学生数；

 select course_id, count(1) from score group by course_id;

#　　33、查询选修了2门以上课程的全部学生的学号和姓名；

SELECT a.student_id ,b.sname 
from score a,student b
where a.student_id=b.sid
group by a.student_id
HAVING count(DISTINCT a.course_id)>2;

#　　34、查询男生、女生的人数，按倒序排列；
    select gender,count(sid) as count_student
    from student
    group by gender
    order by count_student desc;

#　　35、查询姓“张”的学生名单；
  select sname from student where sname like '张%';

　#　36、查询同名同姓学生名单，并统计同名人数；
    select sname,count(1) as count 
    from student group by sname HAVING count(1)>1;


#　　37、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

    select course_id,avg(ifnull(score,0)) as avg 
    from score 
    group by course_id 
    order by avg     asc,course_id desc;


　#　38、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
    select student.sname,score.score 
    from score 
    left join course 
    on score.course_id = course.cid
    left join student 
    on score.student_id = student.sid
    where score.score < 60 and course.cname = '数学';


　#　39、查询课程编号为“3”且课程成绩在80分以上的学生的学号和姓名；

    select student.sid,student.sname from score , student 
    where score.student_id = student.sid
    and  score.course_id = 3 and score > 80;

#　　40、求选修了课程的学生人数

SELECT count(DISTINCT student_id) from score ;

　#　41、查询选修“王五”老师所授课程的学生中，成绩最高和最低的学生姓名及其成绩；
    select sname,score from score 
    left join student 
    on score.student_id = student.sid
    INNER JOIN   (select course.cid from course left join teacher on course.tearch_id = teacher.tid where tname='王五')  c
    on score.course_id=c.cid
    order by score desc limit 1;


#　　42、查询各个课程及相应的选修人数；
SELECT a.cname,count(b.student_id) from course a 
LEFT JOIN score b
on a.cid=b.course_id
GROUP BY a.cid;



　#　43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
   select DISTINCT s1.student_id,s2.student_id, s1.course_id,s2.course_id,s1.score,s2.score 
   from score as s1, score as s2 
   where s1.score = s2.score and s1.course_id <> s2.course_id;



　#　44、查询每门课程成绩最好的前两名学生id和姓名；
SELECT a.student_id, a.course_id, a.score FROM score AS a WHERE 
(SELECT COUNT(DISTINCT score) FROM score AS b 
WHERE b.course_id = a.course_id AND b.score >= a.score) <= 2 
ORDER BY a.course_id ASC, a.score DESC;


　#　45、检索至少选修两门课程的学生学号；
 select student_id from score group by student_id having count(student_id) > 1;

#　　46、查询没有学生选修的课程的课程号和课程名；

SELECT a.cid,a.cname 
from course a 
LEFT JOIN  score b
on a.cid=b.course_id
where b.sid is null ;


#　　47、查询没带过任何班级的老师id和姓名；

SELECT a.tid,a.tname from teacher a
LEFT JOIN teach2cls b
on a.tid=b.tid
where b.tid is null 



#　　48、查询有两门以上课程超过80分的学生id及其平均成绩；       
   

 select a.student_id,avg(a.score) as avg_score
 from score a,
(select student_id from score
 where score>80
 group by student_id
 having count(score.course_id)>2
  )b
 where a.student_id=b.student_id
 group by a.student_id;





#　　49、检索“3”课程分数小于60，按分数降序排列的同学学号；


SELECT
	student_id,
	score
FROM
	score
WHERE
	score < 60
AND course_id = 3
ORDER BY
	score DESC;


　#　50、删除编号为“2”的同学的“1”课程的成绩；


DELETE from   score where student_id=2 and course_id=1;

　#　51、查询同时选修了物理课和生物课的学生id和姓名；

    SELECT e.sid,e.sname from student e,        
    (
    SELECT a.student_id
    from score a , course b 
    where b.cname in ('物理' ,'生物') and a.course_id=b.cid
    GROUP BY a.student_id
    HAVING count(DISTINCT a.course_id)=2) f
    where e.sid=f.student_id;

