#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

import socket

if __name__ == "__main__":
    # 创建套接字
    """ 
    AF_INET:IPv4的IP地址协议
    SOCK_STREAM:tcp传输协议    
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 与server套接字建立连接
    """
    参数为元组，元组第一项为server的ip地址，格式为字符串，第二项为端口号，格式为数字。
    """
    client_socket.connect( ("10.100.13.136", 8080) )
    while True:
        # 发送数据（二进制）
        send_data = input("you have connected with the server, what do you wanna say:")
        client_socket.send( send_data.encode("utf-8") )
        # 接收数据（二进制）
        """
        参数为最大接收字节数（1024）
        """
        recv_data = client_socket.recv(1024).decode("utf-8")
        print("接受到的数据为：", recv_data)
        # 设置结束连接条件
        if send_data == "I am done" and recv_data == "OK":
            break
    # 关闭套接字
    client_socket.close()


"""
总结：client通信：
    1. 创建套接字
    2. 与server套接字建立连接
    3. 发送数据（二进制）
    4. 接收数据（二进制）
    5. 关闭套接字
"""