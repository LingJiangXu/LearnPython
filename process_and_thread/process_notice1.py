#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
from os import getpid, getppid
from multiprocessing import Process, current_process
# import multiprocessing

# 定义全局变量
g_list = list()

# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        sleep(0.2)
    # 代码执行到此，说明数据添加完成。
    print("add_data:", g_list)

def read_data():
    print("read_data:", g_list)

if __name__ == "__main__":
    # 创建添加数据的子进程
    add_data_process = Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = Process(target=read_data)

    add_data_process.start()
    # 主进程等待添加数据的子进程完成后程序再往下执行，读取数据
    add_data_process.join()
    read_data_process.start()


    print("main:",g_list)

    # 总结：多进程间不共享全局变量
