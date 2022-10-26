#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
from os import getpid, getppid
from multiprocessing import Process, current_process

# 定义执行10秒的程序
def task():
    for i in range(10):
        sleep(1)
        print("子进程进行到%d秒"%(i+1))
    print("子程序执行完毕！")


if __name__ == "__main__":
    sub_process = Process(target = task)
    # 设置守护主进程，主进程结束子进程自动销毁
    sub_process.daemon = True
    sub_process.start()

    # 主程序执行2秒完成
    for i in range(4):
        sleep(0.5)
        print("主程序已执行%s秒"%(i*0.5+0.5))
    print("主程序执行完毕！")
    # # 主进程一结束就销毁子进程
    # sub_process.terminate()
    exit()

"""
总结：主进程会等待子进程执行完成再退出
    若要主进程不等待，须在主进程结束时杀掉子进程或者设置守护主进程
"""