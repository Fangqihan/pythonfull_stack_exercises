"""
增加：
add staff_table Alex Li,25,134435344,IT,2015‐10‐29
    步骤：
        1、分析query语句：将数据处理成特定格式；
        2、加载文件数据转换成特定格式；
        3、判断记录唯一性，并写入文件；
        4、返回受影响行数。

删除：
del from staff where id=3
    步骤：
        1、分析query语句：解析出key、value、operator；
        2、加载文件数据转换成特定格式；
        3、根据分析结果并根据条件进行处理，并写入文件；
        4、返回受影响行数。

修改：
UPDATE staff_table SET dept="Market" WHERE dept = "IT" 把所有dept=IT的纪录的dept改成Market
UPDATE staff_table SET age=25 WHERE name = "Alex Li" 把name=Alex Li的纪录的年龄改成25
    步骤：
        1、分析query语句：解析出key、value、operator；
        2、加载文件数据转换成特定格式；
        3、根据分析结果并根据条件进行处理，并写入文件；
        4、返回受影响行数。

查询：
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"
    步骤：
        1、分析query语句：解析出key、value、operator；
        2、加载文件数据转换成特定格式；
        3、根据分析结果进行循环筛选匹配，取出受影响的行数；
        4、返回受影响行数。
"""


def loads_db():
    ret_data = []
    with open('db.txt','r',encoding='utf-8') as f:
        for line in f:
            item = {}
            line_lst = line.strip().split(',')
            item['id']=int(line_lst[0])
            item['name']=line_lst[1]
            item['age']=int(line_lst[2])
            item['phone']=line_lst[3]
            item['dept']=line_lst[4]
            item['enroll_date']=line_lst[5]
            ret_data.append(item)
    # for i in ret_data:
    #     print(i)
    return ret_data


def parse_query(query):
    query = query.strip().split(' ')
    search_key = query[-3]
    search_val = query[-1]
    operator = query[-2]
    if operator not in VALID_OPERATOR: operator = None
    if not search_key or not search_val or operator not in ['=','<','>','like']:
        raise Exception('命令输入有误')
    pass


if __name__ == '__main__':
    VALID_OPERATOR = ['=','<','>','like','>=','<=']
    ret_data = loads_db()






