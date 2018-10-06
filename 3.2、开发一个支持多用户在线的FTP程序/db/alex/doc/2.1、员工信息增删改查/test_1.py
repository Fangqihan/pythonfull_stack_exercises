"""
# p1  >> age > 22
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"

# p2
UPDATE staff_table SET dept="Market" WHERE dept = "IT" 把所有dept=IT的纪录的dept改成Market
UPDATE staff_table SET age=25 WHERE name = "Alex Li" 把name=Alex Li的纪录的年龄改成25

# p3
del from staff where id=3

# p4
add staff_table Alex Li,25,134435344,IT,2015‐10‐29


patterns = [(p1,add),(p2,delete),(p3,update),(p4,find)]
match_status = False

for p in patterns:
    if re.match(p[0],s):
        if p[1] == 'add':
            1、处理当前记录成特定格式；
            2、将当前记录写入到数据库；

        elif p[1] == 'find':
            1、取出key、value、operator
            2、循环ret_data，逐行匹配，返回匹配行数

        elif p[1] in ['update','del']:
            1、取出key、value、operator
            2、循环ret_data,逐行匹配，删除或修改匹配到的行；
            3、将处理后的ret_data写入数据库
        match_status = True

if not match_status: raise Exception('语句语法有误！')

"""


'''
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"
del from staff where id=3

update staff_table set dept="Market" where dept = "IT" 把所有dept=IT的纪录的dept改成Market
update staff_table set age=25 where name = "Alex Li" 把name=Alex Li的纪录的年龄改成25

add staff_table Alex Li,25,134435344,IT,2015‐10‐29
'''

# s_find = 'add staff_table Alex Li,25,134435344,2015‐10‐29'

import re

FIND_PATTERN = 'find [\w|,|*]+ from staff_table where (.+)(>|<|>=|<=|=|like)(.+)'
DEL_PATTERN = 'del from staff where (.+)(>|<|>=|<=|=|like)(.+)'
UPDATE_PATTERN = 'update staff_table set (.+)=(.+) where (.+)(>|<|>=|<=|=|like)(.+)'
ADD_PATTERN = 'add staff_table (.+),(.+),(.+),(.+),(.+)'
PATTERN_LIST = [(FIND_PATTERN, 'find'), (DEL_PATTERN, 'delete'), (UPDATE_PATTERN, 'update'), (ADD_PATTERN, 'add')]


def del_or_find(key, operator, val, type):
    """删除或查询"""
    if type == 'find':
        pass
    elif type == 'delete':
        pass


def add_line(**kwargs):
    pass


if __name__ == '__main__':
    print('\033[1;35m ---------欢迎来到员工管理系统----------- \033[0m')
    while True:
        query = input('>>> ').strip()
        if query.lower() in ['q', 'quit']: exit('Bye!')
        if not query: continue
        for item in PATTERN_LIST:
            m = re.match(item[0], query)
            if m:
                try:
                    if item[1] == 'update':  # 更新逻辑
                        new_key, new_val, key, operator, val = m.groups()
                        print('data>>> ', new_key, new_val, key, operator, val)

                    elif item[1] == 'add':  # 增加逻辑
                        name, age, phone, dept, enroll_date = m.groups()
                        print('data>>> ', name, age, phone, dept, enroll_date)
                        add_line()

                    else:  # 删除和查询逻辑
                        key, operator, val = m.groups()
                        print('data>>> ', key, operator, val)
                        del_or_find(key, operator, val, item[1])

                except Exception as e:
                    print('\033[1;31m syntax error,please check! \033[0m!')
                    break


