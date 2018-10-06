1.用户加密认证；
2.允许同时多用户登录；

3.每个用户有自己的家目录，且只能访问自己的家目录；
    1、根据username:
        def get_or_create(username):
            # 进入自己的home目录
            return




4.对用户进行磁盘配额，每个用户的可用空间不同；
5.允许用户在ftp server上随意切换目录；
6.允许用户查看当前目录下文件；
7.允许上传和下载文件，保证文件一致性(md5)；
8.文件传输过程中显示进度条；
9.附加功能：支持文件的断点续传；

1.在之前开发的FTP基础上，开发支持多并发的功能
2.必须用到队列Queue模块，实现线程池
3.允许配置最大并发数，比如允许只有10个并发用户

思路：
1、cs架构构建：多客户端通讯；

2、用户认证与用户信息数据结构构建：
auth_db = {
'alex':{password:'abc123',mobile:12121212,'login_status':0, 'session_id':None, 'capacity':100,},

'bob':{password:'abc123',mobile:223423784, 'login_status':0, 'session_id':None, 'capacity':100},
}

def auth():
    while True:
        username = input('username>> ').strip()
        password = input('password>> ').strip()
        if not username or not password: continue
        if 认证失败:
            print('用户名或密码有误')
            continue
        item['login_status'] = 1
        item['session_id'] = uuid.uuid4()
        return (user, session_id)









