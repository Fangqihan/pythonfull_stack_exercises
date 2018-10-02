"""
函数、装饰器、迭代器、内置方法
"""

def extract(com):
    """提取主要信息"""
    com = com.strip().split(' ')
    search_key = com[-3]
    search_val = com[-1]
    operator = com[-2]
    if operator not in valid_operator: operator = None
    if not search_key or not search_val or operator not in valid_operator:
        raise Exception('命令输入有误')
    return (search_key, search_val, operator)


def save_db(**kwargs):
    """
    保存数据到文件
    """
    lines_count = 0
    # update
    # delete
    if kwargs.get('after_delete',''):
        ret_data = kwargs.get('after_delete','')
        with open('info_save.txt', 'w') as f:
            for item in ret_data:
                line = str(','.join([str(i) for i in list(item.values())]) + '\n')
                f.write(line)
                f.flush()
                lines_count += 1

    # add
    if kwargs.get('temp',''):
        temp = kwargs.get('temp', '')
        lines_count = 0
        with open('info_save.txt', 'a') as f:
            line = str(','.join([str(i) for i in list(temp.values())]) + '\n')
            f.write(line)
            f.flush()


def load_db():
    """
    加载数据
    [{id:'',name:'',age:2,phone:'',dept:'',enroll_date:''},{},]
    """
    ret_data = []
    with open('info_save.txt', 'r') as f:
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
    return ret_data


def process_data(**kwargs):
    """查询数据"""
    ret_data = load_db()
    lines_count = 0
    operator = kwargs.get('operator')
    search_key = kwargs.get('search_key')
    search_val = kwargs.get('search_val')
    type = kwargs.get('type')

    if operator == 'like':
        for item in ret_data:
            if str(search_val) in item[search_key].lower():
                lines_count += 1
                ret_data.remove(item)
                continue

    elif operator in ['>','<','=']:
        for item in ret_data:
            if operator == '=':
                com = '%s %s %s' % (item[search_key], '==', search_val)
            else:
                com = '%s %s %s' % (item[search_key], operator, search_val)
            if not eval(com):
                continue
            lines_count += 1
            ret_data.remove(item)

    save_db(after_delete = ret_data)
    return lines_count


def find_(com):
    """根据com命令查询出相匹配的记录行数目
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT"
    find * from staff_table where enroll_date like "2013"
    """
    ret_data = load_db()
    lines_count = 0
    search_key, search_val, operator = extract(com)
    if operator == 'like':
        for item in ret_data:
            if str(search_val) in item[search_key].lower():
                lines_count += 1
                continue
        return lines_count
    for item in ret_data:
        if operator == '=':
            com = '%s %s %s' % (item[search_key], '==', search_val)
        else:
            com = '%s %s %s' % (item[search_key], operator, search_val)
        if not eval(com):
            continue
        lines_count += 1
    return lines_count


def update_(com):
    pass


def delete_(com):
    """del from staff where id = 3"""
    search_key, search_val, operator = extract(com)


def add(com):
    """ add staff_table Alex Li,25,134435344,IT,2015‐10‐29"""
    ret_data = load_db()
    lines_count = 0
    info = com.split(' ',2)[2].split(',')
    try:
        temp = {}
        temp['id'] = str(len(ret_data)+1)
        temp['name'] = info[0]
        temp['age'] = info[1]
        temp['phone'] = info[2]
        temp['dept'] = info[3]
        temp['date'] = info[4]
        save_db(temp=temp)
        return lines_count
    except Exception as e:
        print(e)
    return lines_count


if __name__ == '__main__':
    valid_operator = ['>','<','=','like']
    while True:
        input_str = input('>>> ').strip()
        if not input_str:continue
        if 'find' in input_str: print('匹配行数<%s>' % find_(input_str))
        elif 'add' in input_str: print('影响行数<%s>' % add(input_str))
        elif 'del' in input_str: print('影响行数<%s>' % delete_(input_str))
        elif 'update' in input_str:update_(input_str)
        elif input_str == 'q':exit('Bye!')


