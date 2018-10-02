"""
基础需求：：
1、让用户输入用户名密码
2、认证成功后显示欢迎信息
3、输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
"""


import json
import pickle


# auth_list = [
#     {'username': 'alex', 'password': 'abc123', 'status': 0},
#     {'username': 'kate', 'password': 'abc123', 'status': 0},
#     {'username': 'bob', 'password': 'abc123', 'status': 0},
# ]
#
# with open('auth.pkl','wb') as f:
#     f.write(pickle.dumps(auth_list))


with open('auth.pkl','rb') as f:
    auth_list = pickle.loads(f.read())
    print(auth_list)

# with open('auth_list.json','w') as f:
#     f.write(json.dumps(auth_list))


def auth():
    username_err_count = 0
    pwd_error_count = 0
    flag = True
    with open('auth_list.json','r') as f:
        auth_list = json.loads(f.read(),encoding='gbk')

    while flag:
        if username_err_count>=3:exit('用户名输入次数过多')
        username = input('username >>> ').strip()
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
                        return
                    pwd_error_count +=1

        username_err_count +=1

    exit('输入次数过多,请稍后再尝试！')


# auth()

# f = open('auth_list.json','r')
# auth_list = json.loads(f.read(),encoding='')
# print(auth_list)
