#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
import multiprocessing
from os import getpgid, getppid

# 带有参数的任务
def task1(count):
    for i in range(count):
        print("第{}次任务1执行中......".format(i+1))
        sleep(0.2)
    else:
        print("任务1执行完成。")
        
def task2(count):
    for i in range(count):
        print("第{}次任务2执行中......".format(i+1))
        sleep(0.2)
    else:
        print("任务2执行完成。")

if __name__ == "__main__":
    # 创建子进程
    # args:以元组的方式给任务传入参数(元组内容为位置参数传入)
    sub_process1 = multiprocessing.Process(target = task1, args = (5,))
    sub_process1.start()
    # kwargs:表示以字典方式传入参数（字典内容为关键字参数传入）
    sub_process2 = multiprocessing.Process(target = task2, kwargs = {"count":3})
    sub_process2.start()