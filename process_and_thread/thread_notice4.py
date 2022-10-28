#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from threading import Thread, Lock
from time import sleep

g_num = 0    # 定义初始全局变量
lock = Lock()    # 创建全局互斥锁

# 循环一次加1
def write1_task():
    for i in range(1_000_000):
        lock.acquire()   ## 上锁
        global g_num    # 切记，在函数内修改全局变量需要"global"声明！
        g_num += 1
        lock.release()    ## 释放锁
    print("write1:",g_num)

# 循环一次加1
def write2_task():
    global g_num
    for i in range(1_000_000):
        lock.acquire()    ## 上锁
        g_num += 1
        lock.release()    ## 释放锁
    print("write2:",g_num)

if __name__ == "__main__":
    write1_thread = Thread(target=write1_task)
    write2_thread = Thread(target=write2_task)

    # 查看全局变量情况
    print("--------------at first:",g_num)
    write1_thread.start()
    # write1_thread.join()    ## 主线程等待thread1结束再继续执行。(结果就是thread2等待thread1结束再开始。)
    write2_thread.start()
    
    write1_thread.join()
    write2_thread.join()
    print("--------------at last:",g_num)

"""
总结：多线程同时对全局数据操作出现错误！与预想结果不符！
"""
"""
原因：
    在thread1和thread2同时对g_num(假设为0)加1时，会出现：
    1. thread1获取g_num=0,然后cup将thread1调度为“sleeping”状态，把thread2调度为"running"状态。
    2. 接着thread2获取g_num=0，并将得到的值加1赋予g_num，然后系统将thread2调度为"sleeping"，把thread1调度为"running"状态。
    3. thread1将得到的值加1赋予g_num。
    4. 于是thread1和thread2都对g_num加1，但结果为g_num=1。
"""
"""
解决办法：1. ".join()"线程等待。 2. 互斥锁
"""
