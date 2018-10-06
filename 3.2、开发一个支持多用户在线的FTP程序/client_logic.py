import socket
import os
import json

#  \033[1;35m test \033[0m


# BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db')
# SAVE_PATH = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'


def start_client(ip,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    while True:
        # 1、用户认证
        print('\033[1;32m用户认证.... \033[0m')
        login_user = input('username >>> ').strip()
        if not login_user: continue
        auth_data = {'username':login_user}
        client.send(json.dumps(auth_data).encode('utf8'))
        print('\033[1;32m等待验证结果... \033[0m')

        rev_data = client.recv(1024)
        rev_data = json.loads(rev_data.decode('utf8'))
        print('\033[1;3m收到验证结果<%s>... \033[0m' % rev_data)
        if rev_data.get('status') == 1001:
            print('\033[1;34m 验证失败... \033[0m')
            continue

        elif rev_data.get('code') == 1000:
            print('\033[1;33m 验证通过... \033[0m')
            # 2、home目录界面展示
            try:
                BASE_DIR = rev_data['data']['BASE_DIR']
                current_path = [BASE_DIR, login_user]  # 初始化目录为Home目录

                while True:
                    # 1.1、判断最新的current_path是否是文件
                    if not os.path.isdir(os.path.join(*current_path)):
                        # 1.1.1、若用户home目录不存在则新建
                        if len(current_path) == 2:
                            if not os.path.exists(os.path.join(*current_path)):
                                for i in ['audio', 'doc', 'media']:
                                    os.makedirs(os.path.join(*current_path, i))
                        while True:
                            download_choice = input('是否下载y >>').strip()
                            if not download_choice: continue
                            if download_choice.lower() in ['y', 'yes']:
                                # download(current_path, SAVE_PATH)
                                current_path.pop()
                                break

                    # 1.2、是目录则打印当前目录
                    print('\n' + '\033[1;32m %s \033[0m' % os.path.join(*current_path))
                    for f in os.listdir(os.path.join(*current_path)):
                        print('\033[1;35m %s \033[0m' % f)

                    # 2、选择目录或文件
                    com = input('>>> ').strip()  # 命令输入

                    if not com:
                        continue
                    elif com.lower() in ['q', 'quit']:
                        exit('Bye!')

                    # 3.1、选择返回上一层目录
                    elif com.lower() in ['b', 'back']:
                        if len(current_path) > 2:
                            current_path.pop()
                        continue
                    if not com in os.listdir(os.path.join(*current_path)):  # 输入内容不在与当前目录下文件不匹配则无效
                        continue

                    current_path.append(com)  # 3.2、更新current_path，进入下一层目录

            except Exception as e:
                print(e)
                print('对不起,无权限访问！')


        # client.send(b'asasdasdasdasd')

        # msg = input(">> ").strip()
        # if not msg: continue
        # client.send(msg.encode('utf8'))
        # data = client.recv(1024)
        # print('接收信息<%s>' % data.decode('utf8'))
        # if msg == 'q': exit('Bye!')


    # 模拟已经在home目录下找到要下载的文件，并取出文件路径 file_path
    # input('开始下载数据 >>> ')
    # file_path = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\db\alex\audio\2011_美.看不见的竞争力_02.mp4'
    # from_f = open(file_path, 'rb')
    #
    #
    # data = from_f.read(1024)
    # total_len = len(data)
    # print(total_len)  # byte
    # file_name = file_path.strip().split('\\')[-1]



if __name__ == '__main__':
    IP = '127.0.0.1'
    PORT = 8802
    SAVE_PATH = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'
    start_client(IP,PORT)


