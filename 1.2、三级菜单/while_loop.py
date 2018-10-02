
menu = {
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

"""
需求：
1、可依次选择进入各子菜单
2、可从任意一层往回退到上一层
3、可从任意一层退出程序

所需新知识点：列表、字典
"""

import json

# with open('menus.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(menu))

# with open('menus.json','r',encoding='utf-8') as f:
#     menus = json.loads(f.read())
#     print(menus)



def pro():
    menu_1 = list(menu.keys())
    flag1 = True
    while flag1:
        choose_1 = input('一级菜单,请从%s选择 >>> ' % menu_1).strip()
        if choose_1 == 'quit' or choose_1 == 'q':exit('退出程序')
        if not choose_1 in menu_1:continue

        if choose_1 in menu_1:
            flag2 = True
            while flag2:
                menu_2 = list(menu[choose_1].keys())
                if not menu_2:
                    flag2 = False
                    continue
                choose_2 = input('二级菜单，请从%s选择 >>> ' % menu_2)
                if choose_2 == 'quit' or choose_2 == 'q': exit('退出程序')
                if choose_2 == 'b':
                    flag2 = False
                    continue
                if not choose_2 in menu_2: continue
                if choose_2 in menu_2:
                    flag3 = True
                    while flag3:
                        menu_3 = list(menu[choose_1][choose_2].keys())
                        if not menu_3:
                            flag3 = False
                            continue
                        choose_3 = input('三级菜单，请从%s选择 >>> ' % menu_3)
                        if choose_3 == 'b':
                            flag3 = False
                            continue
                        if choose_3 == 'quit' or choose_3 == 'q': exit('退出程序')
                        if not choose_3 in menu_3: continue

                        if choose_3 in menu_3:
                            flag4 = True
                            while flag4:
                                if not menu_3:
                                    flag4=False
                                    continue
                                menu_4 = list(menu[choose_1][choose_2][choose_3].keys())
                                choose_4 = input('请在%s中选择 ' % menu_4)
                                if choose_4 == 'quit' or choose_4 == 'q': exit('退出程序')
                                if choose_4 =='b':
                                    flag4 = False
                                    continue
                                if choose_4 in menu_4:
                                    exit('您已选择< %s >' % choose_4)


if __name__ == '__main__':
    pro()














