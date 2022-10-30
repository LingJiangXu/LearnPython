#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

import socket
import threading

def handle(service_socket, ip_port):
    while True:
        # 接收信息 
        recv_data = service_socket.recv(3072)
        if recv_data:
            print("received : ", recv_data.decode("utf-8") , "; ip_port : ", ip_port)
            # 回复信息
            send_content = "问题正在处理..."
            service_socket.send(send_content.encode("utf-8"))
        else:
            print("{}客户端下线了".format(ip_port))
            break
    # 关闭连接
    service_socket.close()

if __name__ == "__main__":
    # 建立server套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    server_socket.bind( ("", 8080) )
    # 设置监听
    server_socket.listen(12)
    while True:
        # 等待连接请求
        service_socket, ip_port = server_socket.accept()
        print("Have Connected by : ", ip_port)
        # 以子线程运行
        service_socket_thread = threading.Thread(target=handle, args=(service_socket, ip_port))
        service_socket_thread.setDaemon(True)
        service_socket_thread.start()

    # 关闭server套接字
    server_socket.close()


"""
总结：同时响应多个客户端请求（基于服务端通信）：
        1. 循环等待连接
        2. 连接成功就创建子线程专门处理，防止主线程阻塞
        3. 设置守护主线程，防止主线程无法退出
"""