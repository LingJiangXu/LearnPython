#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"


import time
import os
import multiprocessing

# dancing task
def dance():
    # 获取当前进程的编号
    print("the process number of dance:", os.getpid())
    # 获取当前进程的父进程的编号
    print("the parent process number of dance:", os.getppid())
    # 获取当前进程
    print("the dance:", multiprocessing.current_process())
    for i in range(5):
        print("dancing...")
        time.sleep(0.2)

# singing task
def sing():
    # 获取该进程编号
    print("the process number of sing:", os.getpid())
    # 获取该进程的父进程的编号
    print("the parent process number of sing:", os.getppid())
    # 获取当前进程
    print("the sing:", multiprocessing.current_process())
    for i in range(5):
        print("singing...")
        time.sleep(0.2)

if __name__ == "__main__":
    # group：表示进程组，目前只能用None
    # target：表示执行的目标任务名（函数名、方法名）
    # name：进程名称，默认是process-1，...
    dance_process = multiprocessing.Process(target = dance, name = "myprocess1", group = None)
    sing_process = multiprocessing.Process(target = sing)

    # 启动子进程执行相应程序的任务
    dance_process.start()
    sing_process.start()

    # 获取主进程编号(注意，此处先执行主进程)
    print("the process number of mian:", os.getpid())
    # 获取主进程的父进程的编号（为何不是None）
    print("the parent process number of mian:", os.getppid())
    # 获取当前进程
    print("the main:", multiprocessing.current_process())