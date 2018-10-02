

def pro(menus, COUNT):
    COUNT +=1
    menu = list(menus.keys())
    flag = True
    while flag:
        print('当前在%s级别菜单' % COUNT)
        if not menu:
            flag = False
            print('下级菜单为空，请重新选择！')
            continue
        choose = input('请从%s中选择 >>> ' % menu).strip()
        if choose == 'quit' or choose == 'q':exit('退出程序')
        if choose == 'b':
            flag=False
            continue
        if not choose in menu:continue
        if COUNT == 4 and choose in menu:
            exit('您已选择<%s>' % choose)
        if choose in menu:
            pro(menus[choose], COUNT)


menus = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

if __name__ == '__main__':
    COUNT = 0
    pro(menus, COUNT)
