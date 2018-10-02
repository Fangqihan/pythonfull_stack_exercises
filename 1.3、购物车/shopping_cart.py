"""
数据结构：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
......
]

功能要求：
基础要求：

1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

扩展需求：

1、用户下一次登录后，输入用户名密码，直接回到上次的状态，
即上次消费的余额什么的还是那些，再次登录可继续购买。

2、允许查询之前的消费记录
"""

goods_list = [
    {'number':'001',"name": "mac_pro", "price": 12000},
    {'number':'002',"name": "mac_air", "price": 6000},
    {'number':'003',"name": "mouse", "price": 120},
    {'number':'004',"name": "headset", "price": 200},
    {'number':'005',"name": "keyboard", "price": 300},
]


import json
with open('goods.json','w') as f:
    f.write(json.dumps(goods_list))

def auth(func):
    """装饰器 用户认证"""
    def inner():
        username_err_count = 0
        pwd_error_count = 0
        flag = True
        with open('auth_list.json','r') as f:
            auth_list = json.loads(f.read(),encoding='gbk')
        while flag:
            if username_err_count>=3:exit('用户名输入次数过多')
            username = input('username >>> ').strip().lower()
            if not username : continue  # 都不能为空
            for item in auth_list:
                if item.get('username','') == username:
                    if item.get('status')==1:
                        exit('对不起，账户< %s >以被锁定，请前往网点解锁！' % username)

                    while True:
                        if pwd_error_count >=3:
                            item['status']=1
                            with open('auth_list.json','w') as f:
                                f.write(json.dumps(auth_list))
                            exit('密码输入次数过多，账户被锁定，请前往相关网点解锁！')

                        pwd = input('password >>> ').strip()
                        if pwd == item.get('password',''):
                            print('欢迎登录，%s' %  username)
                            cart_history = item.get('shopping_history','')
                            balance = item.get('balance','')
                            func(cart_history=cart_history,balance=balance,username=username)
                            return
                        pwd_error_count +=1
            username_err_count +=1
        print('输入次数过多,请稍后再尝试！')
    return inner


def goods_display():
    print('NUMBER'.ljust(10),'NAME'.ljust(15),'PRICE'.ljust(10))
    for item in goods_list:
        print(item['number'].ljust(10),item['name'].ljust(15),str(item['price']).ljust(10))


def save(**kwargs):
    username = kwargs.get('username')
    cart_history = kwargs.get('cart_history')
    balance = kwargs.get('balance')
    with open('auth_list.json','r') as f:
        auth_list = json.loads(f.read())
        for item in auth_list:
            if item['username'] == username:
                item['balance'] = balance
                item['shopping_history'] = cart_history

    with open('auth_list.json','w') as f:
        f.write(json.dumps(auth_list))


@auth
def shopping_cart(**kwargs):
    cart_history = kwargs.get('cart_history')
    balance = kwargs.get('balance')
    username=kwargs.get('username')
    # print(cart_history, balance, username)

    goods_display()
    flag = True
    while flag:
        choose = input('>>> ').strip()
        for item in goods_list:
            if item['number'] == choose:
                if balance<item['price']:
                    print('余额不足！')
                    continue
                cart_history.append(item['name'])
                balance = balance - item['price']

        if choose.lower()=='q':
            save(username=username,cart_history=cart_history,balance=balance)
            exit('您的余额<\033[1;35m %s \033[0m>,已购商品<\033[1;35m %s \033[0m>!'%(balance,'、'.join(cart_history)))

        elif choose.lower() == 'info':
            print('您的余额<\033[1;35m %s \033[0m>,已购商品<\033[1;35m %s \033[0m>'%(balance,'、'.join(cart_history)))


if __name__ == '__main__':
    shopping_cart()










