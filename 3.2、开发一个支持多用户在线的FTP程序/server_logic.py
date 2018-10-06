import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import os
import json


def handle_msg(conn):
    print('\033[1;31m 开启子线程<%s>.... \033[0m' % threading.current_thread())
    while True:
        import time
        time.sleep(1)
        data = conn.recv(1024)
        if not data:break
        data = json.loads(data.decode('utf8'))  # 1、接收验证信息
        print('\033[1;35m 收到数据<%s>, 开始验证.... \033[0m' % data)
        if not data: break
        if data.get('username') in ['alex','bob','kate']:
            # 传输目录信息
            data = {'code':1000,'data':{'BASE_DIR':BASE_DIR}}
            print('\033[1;35m 返回数据<%s>.... \033[0m' % data)
            conn.send(json.dumps(data).encode('utf8'))
        else:
            conn.send(json.dumps({'code':1001}).encode('utf8'))
            continue
        if not data: break

        msg = conn.recv(1024)  # 2、
        print('接收信息<%s>' % data)
        conn.send(data.lower().encode('utf-8'))


    # # 模拟循环接收数据
    # to_path_dir = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'
    # from_f = open(file_path, 'rb')
    # data = from_f.read(1024)  #
    # total_len = len(data)
    # print(total_len)  # byte
    # file_name = file_path.strip().split('\\')[-1]


def start_server(ip, port):
    """启动服务器"""
    print('\033[1;34m 启动服务器.... \033[0m')
    t_pool = ThreadPoolExecutor(3)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    while True:
        print('\033[1;34m 等待客户端连接.... \033[0m')
        conn, addr = server.accept()
        t_pool.submit(handle_msg, conn)


if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db')
    SAVE_PATH = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'
    IP = '127.0.0.1'
    PORT = 8802
    start_server(IP, PORT)


