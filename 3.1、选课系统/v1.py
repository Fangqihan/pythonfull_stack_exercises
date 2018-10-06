from datetime import date
import pickle


class Common(object):
    """继承类，整合共用的方法"""
    @classmethod
    def list_display(cls):
        """打印传入类的所有实例化对象"""
        print('---------%s列表----------' % cls.__name__)
        db_name = '%ss.pkl' % str(cls.__name__).lower()
        with open(db_name, 'rb') as f:
            obj_list = pickle.loads(f.read())
            for obj in obj_list: print(obj.name)

    @classmethod
    def obj_list(cls, type):
        db_name = '%ss.pkl' % str(cls.__name__).lower()
        with open(db_name, 'rb') as f:
            if type == 'name':
                obj_list = [obj.name for obj in pickle.loads(f.read())]
            else:
                obj_list = pickle.loads(f.read())
        return obj_list

    @classmethod
    def get_obj(cls,name):
        """根据输入的名称获取对象"""
        db_name = '%ss.pkl' % str(cls.__name__).lower()
        with open(db_name, 'rb') as f:
            obj_list = [obj.name for obj in pickle.loads(f.read())]
            for obj in obj_list:
                if obj.name ==name:
                    return obj

            return None

    @classmethod
    def save(cls, obj):
        """更新当前类对象列表文件"""
        if not isinstance(obj, cls):
            raise Exception('保存的对象与当前类不符合')
        db_name = '%ss.pkl' % str(cls.__name__).lower()
        with open(db_name, 'rb') as f:
            obj_list = pickle.loads(f.read())
        obj_list.append(obj)
        with open(db_name, 'wb') as f:
            f.write(pickle.dumps(obj_list))


class School(Common):
    """校区"""
    def __init__(self, name):
        self.name = '%s校区' % name


print(School.obj_list(type='name'))


class Course(Common):
    """课程"""
    def __init__(self, name, school, price, period):
        self.name = name
        self.school = school
        self.period = period
        self.price = price


class ClassGrade(object):
    """班级"""
    def __init__(self, school, course):
        self.school = school
        self.course = course
        self.name = '%s_%s%s_%s全栈' % (school.name, date.today().year,
                                      date.today().month, course.name)
        # 上海校区201801python全栈


class Student(object):
    def __init__(self,name,school,class_grade):
        self.name = name
        self.school = school
        self.class_grade = class_grade


class Teacher(object):
    def __init__(self,name,course):
        self.name = name
        self.course = course


class ExamResult(object):
    def __init__(self, class_grade,student, score):
        self.class_grade = class_grade
        self.student = student
        self.score = score


class Auth(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password


# import pickle
#
# # 取出所有学校对象
# with open('schools.pkl', 'rb') as f:
#     s1, s2 = pickle.loads(f.read())
#
# # 取出素有课程对象
# with open('courses.pkl', 'rb') as f:
#     c1, c2, c3 = pickle.loads(f.read())
#
# # 取出所有班级
# with open('class_grades.pkl', 'rb') as f:
#     c_g_1, c_g_2, c_g_3 = pickle.loads(f.read())
#
#
# # 取出所有教师对象
# with open('teachers.pkl', 'rb') as f:
#     t1, t2, t3 = pickle.loads(f.read())


# 创建所有班级
# c_g_1 = ClassGrade(s1,c1)
# c_g_2 = ClassGrade(s1,c2)
# c_g_3 = ClassGrade(s1,c3)
# with open('class_grades.pkl','wb') as f:
#     f.write(pickle.dumps([c_g_1,c_g_2,c_g_3]))


# 创建校区
school_1 = School('北京')
school_2 = School('上海')
with open('schools.pkl','wb') as f:
    f.write(pickle.dumps([school_1,school_2]))

# 创建课程
# c1=Course('linux',s1,'20000','6')
# c2=Course('python',s1,'18000','6')
# c3=Course('go',s2,'19000','6')
# with open('courses.pkl','wb') as f:
#     f.write(pickle.dumps([c1,c2,c3]))


# 创建教师
# t1 = Teacher('alex',s1, c1)
# t2 = Teacher('bob',s1, c2)
# t3 = Teacher('kate',s2, c3)
# with open('teachers.pkl','wb') as f:
#     f.write(pickle.dumps([t1,t2,t3]))

# with open('teachers.pkl','rb') as f:
#     obj_list = pickle.loads(f.read())
#     for obj in obj_list:
#         print(obj.name,obj.course.name,obj.course.price,obj.course.period)




