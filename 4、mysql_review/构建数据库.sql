create table class_grade(
  id int auto_increment primary key,
  name char(32)
);

insert into class_grade(name) values
  ('一年级'),
  ('二年级'),
  ('三年级');


create table class(
  id int auto_increment primary key,
  caption char(32) unique,
  grade_id int,
  constraint foreign key class(grade_id) references class_grade(id)
  on delete cascade
  on update cascade
);

insert into class(caption, grade_id) values
  ('一年一班',1),
  ('二年一班',2),
  ('三年一班',3);


create table student(
  id int auto_increment primary key,
  name char(32),
  gender enum('男','女'),
  class_id int,
  constraint foreign key student(class_id) references class(id)
  on delete cascade
  on update cascade
);

insert into student(name, gender, class_id) VALUES
  ('晓燕','女',1),
  ('小熏','女',1),
  ('陈浩','男',2);


create table teacher(
  id int auto_increment primary key,
  name char(32)
);

insert into teacher(name) values
  ('alex'),
  ('agon'),
  ('shanshan');


create table course(
  id int primary key auto_increment,
  name char(32),
  teacher_id int,
  constraint foreign key course(teacher_id) references teacher(id)
  on delete cascade
  on update cascade
);

insert into course(name,teacher_id) values
('linux运维',1),
('python全栈',1),
('java开发',2);


-- 教师与班级m2m关系
create table teacher_to_class(
  id int primary key auto_increment,
  teacher_id int,
  class_id int,
  constraint fk_teacher foreign key teacher_to_class(teacher_id) references teacher(id)
  on delete cascade on
  update cascade,
  constraint fk_class foreign key teacher_to_class(class_id) references class(id)
  on UPDATE cascade
  on delete cascade,
  unique(teacher_id, class_id)
);

insert into teacher_to_class(teacher_id, class_id) VALUES
  (1,1),
  (1,2),
  (2,1),
  (3,2);


create table score(
  id int primary key auto_increment,
  student_id int,
  course_id int,
  score int,
  constraint fk_stu_score foreign key(student_id) references student(id) on delete cascade on update cascade,
  constraint fk_course_score foreign key(course_id) references course(id) on delete cascade on update cascade,
  unique (student_id,course_id)
);

insert into score(student_id, course_id, score) values
  (1, 1, 60),
  (1, 2, 59),
  (1, 3, 80),
  (2, 1, 80),
  (2, 2, 88),
  (2, 3, 90),
  (3, 1, 23),
  (3, 2, 45),
  (3, 3, 80);





