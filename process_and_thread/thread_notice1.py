#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
import threading

def task():
    # 关键！设置线程启动延时
    sleep(2)
    # 打印当前线程名
    print("当前线程名：", threading.current_thread().name)


if __name__ == "__main__":
    # 创建多个线程并执行
    for _ in range(100):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()

"""
总结：同进程一样，线程执行是无序的，进程顺序由操作系统决定，线程顺序由cup决定。
"""