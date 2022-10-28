#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from threading import Thread
from time import sleep

g_list = []    # 定义空列表为初始全局变量

# 向全局变量写入数据
def write_task():
    for i in range(10):
        g_list.append(i) # .append方法为原地操作，可不声明全局变量。若"g_list += [i]"则需要"global"声明！
        print("添加{}完成。".format(i))
        sleep(0.5)
    print("数据写入完成!")

# 向全局变量读取数据
def read_task():
    for i in range(10):
        print("读取列表为：",g_list)
        sleep(0.6)

if __name__ == "__main__":
    write_thread = Thread(target=write_task)
    read_thread = Thread(target=read_task)

    # 启动主进程、写入子线程，读取子线程。查看全局变量情况
    print("--------------at first:",g_list)
    write_thread.start()
    read_thread.start()
    write_thread.join()    # 主线程等待写入子线程结束
    read_thread.join()    # 主线程等待读取子线程结束
    print("--------------at last:",g_list)

"""
总结：线程间共享全剧变量。
"""
