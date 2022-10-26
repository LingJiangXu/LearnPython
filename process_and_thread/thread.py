#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

from time import sleep
import threading

def sing():
    print("当前唱歌的线程为：", threading.current_thread())
    for i in range(5):
        print("Tom is singing...%d" %i)
        sleep(0.8)

def dance():
    print("当前跳舞的线程为：", threading.current_thread())
    for i in range(6,11):
        print("Lucy is dancing...%d" %i)
        sleep(0.8)


if __name__ == "__main__":
    print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌子线程
    sing_thread = threading.Thread(target = sing)
    # 创建跳舞子线程
    dance_thread = threading.Thread(target = dance)
    
    sing_thread.start()
    dance_thread.start()
