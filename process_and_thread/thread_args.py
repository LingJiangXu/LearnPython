#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
import threading

def args_task(counts):
    print("the args is:", counts)
    for i in range(counts):
        print("args任务执行中...%d" %i)
        sleep(0.5)
    else:
        print("args任务执行完成")

def kwargs_task(counts):
    print("the kwargs is :", counts)
    for i in range(counts):
        print("kwargs任务执行中...%d" %i)
        sleep(0.5)
    else:
        print("kwargs任务执行完成")

if __name__ == "__main__":
    # 创建子线程，使用元组传参
    args_thread = threading.Thread(target=args_task, args = (6,))
    # 创建子线程，使用字典传参
    kwargs_thread = threading.Thread(target = kwargs_task, kwargs = {"counts":4})

    args_thread.start()
    kwargs_thread.start()