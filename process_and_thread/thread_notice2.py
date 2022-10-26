#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
import threading

def task():
    for i in range(10):
        print("子线程进行至%d/10" %(i+1))
        sleep(0.5)

if __name__ == "__main__":
    sub_thread = threading.Thread(target=task)
    # 设置主线程等待
    sub_thread.setDaemon(True)
    sub_thread.start()

    print("主线程开始：......")
    sleep(2)
    print("主线程结束！！！！！")

"""
总结：主线程同样会等待子线程结束才结束完成！
    同样可以守护主线程实现主线程不等待：
            1.threading.Thread(target=task,daemon = True) 2.sub_thread.setDaemon(True)
"""