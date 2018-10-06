import os


def download(current_path, to_path):
    file_path = os.path.join(*current_path)
    print('开始下载文件....')
    import time
    time.sleep(2)
    print('下载完毕！')



# # 模拟进行分段传输
# file_path = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\db\alex\audio\2011_美.看不见的竞争力_02.mp4'
#
# to_path_dir = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'
#
# # 读取文件内容
# from_f = open(file_path, 'rb')
# data = from_f.read(1024)  #
# total_len = len(data)
# print(total_len)  # byte
# file_name = file_path.strip().split('\\')[-1]


# 写入文件内容
# to_f = open(os.path.join(to_path_dir, file_name), 'a')
# print('开始写入文件...')
# current_len = 0
# while True:
#     while current_len <= total_len:
#         to_f.write(data)
#         current_len += 1024


'''
def operation(username, BASE_DIR, SAVE_PATH):
    """
    1、查看当前目录下的文件
    2、切换目录
    3、选择下载文件
    """
    current_path = [BASE_DIR, username]  # 初始化目录为Home目录
    while True:
        # print(current_path)
        # 1.1、判断最新的current_path是否是文件
        if not os.path.isdir(os.path.join(*current_path)):
            # 1.1.1、若用户home目录不存在则新建
            if len(current_path) == 2:
                if not os.path.exists(os.path.join(*current_path)):
                    for i in ['audio','doc','media']:
                        os.makedirs(os.path.join(*current_path,i))
            while True:
                download_choice = input('是否下载y >>').strip()
                if not download_choice:continue
                if download_choice.lower() in ['y','yes']:
                    download(current_path, SAVE_PATH)
                    current_path.pop()
                    break

        # 1.2、是目录则打印当前目录
        print('\n'+'\033[1;32m %s \033[0m'% os.path.join(*current_path))
        for f in os.listdir(os.path.join(*current_path)):
            print('\033[1;35m %s \033[0m' % f)

        # 2、选择目录或文件
        com = input('>>> ').strip()  # 命令输入
        if not com: continue
        elif com.lower() in ['q', 'quit']: exit('Bye!')

        # 3.1、选择返回上一层目录
        elif com.lower() in ['b', 'back']:
            if len(current_path) > 2:
                current_path.pop()
            continue
        if not com in os.listdir(os.path.join(*current_path)):  # 输入内容不在与当前目录下文件不匹配则无效
            continue

        current_path.append(com)  # 3.2、更新current_path，进入下一层目录
'''



def operation(username, BASE_DIR, SAVE_PATH):
    """
    1、查看当前目录下的文件
    2、切换目录
    3、选择下载文件
    """
    current_path = [BASE_DIR, username]  # 初始化目录为Home目录
    while True:
        # print(current_path)
        # 1.1、判断最新的current_path是否是文件
        if not os.path.isdir(os.path.join(*current_path)):
            # 1.1.1、若用户home目录不存在则新建
            if len(current_path) == 2:
                if not os.path.exists(os.path.join(*current_path)):
                    for i in ['audio','doc','media']:
                        os.makedirs(os.path.join(*current_path,i))
            while True:
                download_choice = input('是否下载y >>').strip()
                if not download_choice:continue
                if download_choice.lower() in ['y','yes']:
                    download(current_path, SAVE_PATH)
                    current_path.pop()
                    break

        # 1.2、是目录则打印当前目录
        print('\n'+'\033[1;32m %s \033[0m'% os.path.join(*current_path))
        for f in os.listdir(os.path.join(*current_path)):
            print('\033[1;35m %s \033[0m' % f)

        # 2、选择目录或文件
        com = input('>>> ').strip()  # 命令输入
        if not com: continue
        elif com.lower() in ['q', 'quit']: exit('Bye!')

        # 3.1、选择返回上一层目录
        elif com.lower() in ['b', 'back']:
            if len(current_path) > 2:
                current_path.pop()
            continue
        if not com in os.listdir(os.path.join(*current_path)):  # 输入内容不在与当前目录下文件不匹配则无效
            continue

        current_path.append(com)  # 3.2、更新current_path，进入下一层目录



# if __name__ == '__main__':
#     BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db')
#     to_path = r'D:\临时文件\master\3.2、开发一个支持多用户在线的FTP程序\downloads'
#     try:
#         operation('alex')
#     except Exception as e:
#         print('对不起,无权限访问！')


'''
3、允许下载文件到本地，保证文件一致性
4、允许上传文件到目录
5、进度条显示
6、文件断点续传
'''
















