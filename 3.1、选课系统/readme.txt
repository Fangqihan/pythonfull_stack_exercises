角色:校长、学员、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含周期、价格，通过学校创建课程；
4. 通过学校创建班级，班级关联课程、讲师；
5. 创建学员时，选择学校，关联班级；
5. 创建讲师角色时要关联学校；
6. 提供两个角色接口；

6.1 学员视图， 可以注册， 交学费， 选择班级；
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ，
    修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里


入口程序：
    def auth(username, password):
            if 通过认证：
                return user

    def create_school():
        name = input('>> ')
        school_obj = School(name)
        School.save(school_obj)

     def create_course():
        School.list_display()
        while True:
            school_name = input('school>> ')
            school_obj = School.get_obj(school_name)
            if not school_obj:
                print('学校名称输入有误')
                continue
            name = input('name>> ')
            price = input('price>> ')
            period = input('period>> ')
            course_obj = Course(name,school_obj, price, period)
            Course.save(course_obj)


    username = input('username>>')
    password = input('password>>')
    user = auth(username, password)

    display_actions(user)
        if user.type == '0':
            # 管理者
            for act in actions:print(act)
            while True:
                choose = input('>> ').strip()
                if choose in actions:
                    return choose()

        elif user.type == '1':
            # 教师
            pass
        elif user.type == '2':
            # 学生
            pass




流程对象构建：
    1、创建学校：s1=School('北京'),s2=School('上海')

    2、创建课程：
        c1=Course('linux',s1,'20000','6')
        c2=Course('python',s2,'18000','6')
        c3=Course('go',s1,'19000','6')
    3、创建班级：
        c_g_1 = ClassGrade('北京_201801_linux',s1,c1)
        c_g_2 = ClassGrade('上海_201801_python',s2,c2)

    4、创建教师：
        t1 = Teacher('alex', s1, c1)
        t2 = Teacher('bob', s2, c2)

    5、创建学生：
        s1 = Student('小陈',s1,c_g_1)
        s2 = Student('小王',s2,c_g_2)

    6、考试成绩记录：
        ret_1 = ExamResult(c_g_1,s1,90)
        ret_2 = ExamResult(c_g_2,s2,88)










