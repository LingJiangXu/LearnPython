#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

import socket

if __name__ == "__main__":
    # 创建server套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## 设置端口号复用
    """SOL_SOCKET：当前套接字 SO_REUSEADDR：设置端口号复用选项 TRUE：设置值"""
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    """一般ip地址不指定，表示本机任一个ip都可"""
    server_socket.bind( ("192.168.56.102", 8080) )
    # 设置监听（不能让client设置监听）（该套接字仅负责监听！）
    """参数为设置最大等待连接个数"""
    server_socket.listen(2)
    # 等待连接请求(程序阻塞直至得到请求)
    """建立专门与client通信的套接字，客户端的ip和端口"""
    service_client_socket, ip_port = server_socket.accept()
    print("此时建立连接成功，客户端的ip地址和端口号为：", ip_port)
    while True:
        # 接收数据
        recv_data = service_client_socket.recv(1024).decode("utf-8")
        print("from client: ", recv_data)
        # 发送数据
        send_data = input("server: ")
        service_client_socket.send(send_data.encode("utf-8"))
        if recv_data == "I am done" and send_data == "OK":
            break
    # 解除连接通信套接字,关闭服务器监听套接字
    service_client_socket.close()
    server_socket.close()

"""
总结：server通信：
    1. 创建server套接字（监听）
    2. 绑定端口
    3. 设置监听
    4. 建立通信套接字
    5. 接收数据
    6. 发送数据
    7. 解除连接通信套接字,关闭服务器监听套接字
"""
"""问题：server退出后，端口号不会立马释放"""
"""解决：1.更换server端口号 2.设置端口号复用"""