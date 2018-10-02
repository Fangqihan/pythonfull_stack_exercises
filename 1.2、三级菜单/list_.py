menus = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

history = []
current = menus

while True:
    for k in current:
        print(k)
    print('history >> ', len(history))
    choose = input('>>> ').strip()
    if choose == 'q' or choose == 'quit':
        exit('exit')
    elif choose in current.keys():
        history.append(current)  # 添加到历史记录列表
        current = current[choose]  # 修改当前current记录
    elif choose == 'b' or choose == 'history':
        current = history.pop()
